import numpy as np

class SecMPC_Stepper:
    def step(self, C, bot, mpc, do_not_execute):
        self.step_count += 1

        # -- iterate
        self.tic.wait_for_tic()

        # -- get optitrack
        if bot.optitrack:
            bot.optitrack.pull(C)

        # -- get current state (time, q, qDot)
        q, q_dot, q_ref, q_dot_ref = np.zeros((4, 1)), np.zeros((4, 1)), np.zeros((4, 1)), np.zeros((4, 1))
        ctrl_time = 0.0
        bot.get_state(q, q_dot, ctrl_time)
        bot.get_reference(q_ref, q_dot_ref, None, q, q_dot, ctrl_time)

        # -- iterate MPC
        mpc.cycle(C, q_ref, q_dot_ref, q, q_dot, ctrl_time)
        mpc.report(C)
        if mpc.phase_switch:
            bot.sound(7 * mpc.timing_MPC.phase)

        if self.fil.is_open():
            self.fil.write(f"{self.step_count} {ctrl_time} {mpc.timing_MPC.phase}\n")
            np.savetxt(self.fil, q, header="q_real", comments="", fmt="%.6f")
            np.savetxt(self.fil, mpc.waypoint_MPC.path, header="waypoints", comments="", fmt="%.6f")
            np.savetxt(self.fil, mpc.timing_MPC.tau, header="tau", comments="", fmt="%.6f")
            np.savetxt(self.fil, mpc.short_MPC.path, header="shortPath", comments="", fmt="%.6f")
            C.get_frame_state(self.log_poses).to_file(self.fil, "poses", comment="#", precision=6)

        # -- send spline update
        if not do_not_execute:
            ctrl_time = bot.get_t()
            sp = mpc.get_short_path(ctrl_time)
            if sp.pts.shape[0]:
                # if sp.times[0] < 0.:
                #     bot.sound(2 * (self.step_count % 12))
                if sp.vels.shape[0]:
                    # bot.move(sp.pts, sp.vels, sp.times, True, ctrl_time)
                    pass
                else:
                    bot.move(sp.pts, sp.times, True, ctrl_time)

        # -- update C
        bot.sync(C, 0.0)
        if bot.key_pressed == 'q' or bot.key_pressed == 27:
            return False

        return True

class SecMPC_Viewer:
    def _init_(self, C):
        self.C = C
        self.C.gl().clear()
        self.C.gl().add(gl_standard_light)
        self.C.gl().add(self)
        if C["camera_gl"]:
            self.set_camera(C.gl(), C["camera_gl"])

    def step(self, mpc):
        self.C.set_frame_state(mpc.waypoint_MPC.komo.world.get_frame_state())
        self.ctrl_time = mpc.ctrl_time_at_last_update
        self.phase = mpc.timing_MPC.phase
        self.q_real = mpc.q_ref_at_last_update
        self.waypoints = mpc.waypoint_MPC.path
        self.tau = mpc.timing_MPC.tau
        self.short_path = mpc.short_MPC.path

        self.C.view()

    def gl_draw(self, gl):
        # C itself
        # gl.draw_options.draw_visuals_only = True
        # gl.draw_options.draw_colors = True
        # self.C.set_joint_state(self.q_real)
        # self.C.set_frame_state(self.poses, self.log_poses)
        # self.C.gl_draw(gl)

        # waypoints
        a = 0.6 / (self.waypoints.shape[0] - 1)
        gl.draw_options.draw_colors = False
        for t in range(self.waypoints.shape[0]):
            glColor(1., 1. - a * t, 0.4 + a * t)
            self.C.set_joint_state(self.waypoints[t])
            self.C.gl_draw(gl)

        # short_path
        # glColor(0.5, 1., 1., .3)
        # gl.draw_options.draw_colors = False
        # for t in range(self.short_path.shape[0]):
        #     self.C.set_joint_state(self.short_path[t])
        #     self.C.gl_draw(gl)

        # text
        text = f"phase: {self.phase} ctrl_time: {self.ctrl_time}\ntau: {self.tau}"
        glColor(0.2, 0.2, 0.2, 0.5)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glOrtho(0., float(gl.width), float(gl.height), 0., -1., 1.)
        gl_draw_text(text, 20, +20, 0, True)

def play_log(logfile):
    C = rai.Configuration()
    C.add_file("pushScenario.g")

    log_poses = C.get_frames(["puck", "target"])
    gl = OpenGL()

    viewer = SecMPC_Viewer(C)
    gl.add(viewer)

    with open(logfile, 'r') as fil:
        k = 1
        while True:
            line = fil.readline()
            if not line:
                break

            tokens = line.split()
            viewer.step_count, viewer.ctrl_time, viewer.phase = map(float, tokens[:3])

            viewer.q_real = np.loadtxt(fil, ndmin=2)
            viewer.waypoints = np.loadtxt(fil, ndmin=2)
            viewer.tau = np.loadtxt(fil, ndmin=2)
            viewer.short_path = np.loadtxt(fil, ndmin=2)
            viewer.poses = np.loadtxt(fil, ndmin=2)

            gl.update()
            rai.wait(0.1)
            k += 1