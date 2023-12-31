body base: { mass: 185.633 }
body head: { X: [0.06, 0, 0.686, 0.707107, 0, -0.707107, 0], mass: 1.02313 }
body right_upper_shoulder: { X: [0.0640272, -0.259027, 0.129626, 0.653281, -0.270599, -0.653281, -0.270599], mass: 8.77895 }
body left_upper_shoulder: { X: [0.0640272, 0.259027, 0.129626, 0.653281, 0.270599, -0.653281, 0.270599], mass: 8.77895 }
body right_lower_shoulder: { X: [0.112818, -0.307818, 0.399976, -0.653282, 0.653282, 0.270597, -0.270597], mass: 7.67181 }
body left_lower_shoulder: { X: [0.112818, 0.307818, 0.399976, -0.270597, 0.270597, 0.653282, -0.653282], mass: 7.67181 }
body right_upper_elbow: { X: [0.184942, -0.379943, 0.399976, 0.923879, 1.32497e-12, -3.19872e-12, -0.382684], mass: 5.52286 }
body left_upper_elbow: { X: [0.184942, 0.379943, 0.399976, 0.923879, 3.19889e-12, -1.32491e-12, 0.382684], mass: 5.52286 }
body right_lower_elbow: { X: [0.370501, -0.565502, 0.330976, -0.653282, 0.653282, 0.270597, -0.270597], mass: 6.27938 }
body left_lower_elbow: { X: [0.370501, 0.565502, 0.330976, -0.270597, 0.270597, 0.653282, -0.653282], mass: 6.27938 }
body right_upper_forearm: { X: [0.44375, -0.638751, 0.330976, 0.923879, 3.58688e-12, -4.13569e-12, -0.382684], mass: 3.24201 }
body left_upper_forearm: { X: [0.44375, 0.638751, 0.330976, 0.923879, 5.46085e-12, -3.87967e-13, 0.382684], mass: 3.24201 }
body right_lower_forearm: { X: [0.635163, -0.830166, 0.320976, -0.653282, 0.653282, 0.270597, -0.270597], mass: 2.74076 }
body left_lower_forearm: { X: [0.635163, 0.830166, 0.320976, -0.270597, 0.270597, 0.653282, -0.653282], mass: 2.74076 }
body right_wrist: { X: [0.71717, -0.912173, 0.320976, 0.923879, 5.8489e-12, -5.07266e-12, -0.382684], mass: 3.22029 }
body left_wrist: { X: [0.71717, 0.912173, 0.320976, 0.923879, 7.72288e-12, 5.4895e-13, 0.382684], mass: 3.22029 }
body r_gripper_l_finger: { X: [0.828221, -1.02535, 0.320976, -0.653282, -0.653282, -0.270597, -0.270597], mass: 0.0526538 }
body r_gripper_r_finger: { X: [0.830342, -1.02322, 0.320976, -0.653282, -0.653282, -0.270597, -0.270597], mass: 0.0526538 }
body l_gripper_l_finger: { X: [0.830342, 1.02322, 0.320976, -0.270597, -0.270597, -0.653282, -0.653282], mass: 0.0553155 }
body l_gripper_r_finger: { X: [0.828221, 1.02535, 0.320976, -0.270597, -0.270597, -0.653282, -0.653282], mass: 0.0553155 }

shape visual (base): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.0286935, -0.000728762, 0.371004, 1, 0, 0, 0], mesh: <torso/base_link.STL>, color: [0.2, 0.2, 0.2, 1], rel_includes_mesh_center, }
shape collision_base (base): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.0648345, 1.53654e-05, 0.172863, 1, 0, 0, 0], contact: -2, mesh: <torso/base_link_collision.STL>, rel_includes_mesh_center, }
shape visual (head): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.0319886, -2.26154e-05, -0.00274816, -0.707107, 0, -0.707107, 0], mesh: <head/H0.STL>, color: [0.2, 0.2, 0.2, 1], rel_includes_mesh_center, }
shape collision_head (head): { shape: sphere, size: [0, 0, 0, 0.001], Q: [-0, -0, -0, -0.707107, 0, -0.707107, 0], contact: -2 }
shape visual (base): { shape: capsule, size: [0, 0, 0.01, 0.085], Q: [0.06, 8.1634e-19, 0.827118, -1, 0, 0, 0], color: [0.2, 0.2, 0.2, 1], rel_includes_mesh_center, }
shape collision_base (base): { shape: sphere, size: [0, 0, 0, 0.001], Q: [0.0947, 0, 0.817, -1, 0, 0, 0], contact: -2 }
shape visual (head): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.0055038, -0.000139031, -0.0938075, -0.453099, -0.453099, -0.542864, 0.542864], mesh: <head/H1.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_head (head): { shape: sphere, size: [0, 0, 0, 0.001], Q: [2.72449e-17, 0, -0.1227, 0.063474, -0.704252, -0.704252, 0.063474], contact: -2 }
shape visual (head): { shape: box, size: [0.218, 0.16, 0.001, 0], Q: [-0.0157421, 1.40048e-14, -0.119839, 0.154854, -0.689942, -0.689942, 0.154854], color: [0, 0, 0, 1] }
shape visual (base): { shape: sphere, size: [0, 0, 0, 0.001], Q: [0.11, 0, 0.75, 1, 0, 0, 0], color: [0.8, 0.3, 0.3, 0.3] }
#shape collision_base (base): { shape: sphere, size: [0, 0, 0, 0.22], Q: [0.04, -0.04, 0.75, 1, 0, 0, 0], contact: -2 }
shape visual (base): { shape: sphere, size: [0, 0, 0, 0.001], Q: [0.11, 0, 0.75, 1, 0, 0, 0], color: [0.8, 0.3, 0.3, 0.3] }
#shape collision_base (base): { shape: sphere, size: [0, 0, 0, 0.22], Q: [0.04, 0.04, 0.75, 1, 0, 0, 0], contact: -2 }
shape visual (right_upper_shoulder): { shape: mesh, size: [1, 1, 1, 1], Q: [0.204968, -0.000259649, -0.0560219, -0.707107, 0, -0.707107, 0], mesh: <upper_shoulder/S0.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_right_upper_shoulder (right_upper_shoulder): { shape: capsule, size: [0, 0, 0.2722, 0.06], Q: [0.152112, -1.33336e-18, 3.36804e-17, -0.707107, 0, -0.707107, 0], contact: -2, rel_includes_mesh_center, }
shape visual (right_lower_shoulder): { shape: mesh, size: [1, 1, 1, 1], Q: [6.04869e-05, -2.01515e-05, -0.0561637, -0.707107, 0, -0.707107, 0], mesh: <lower_shoulder/S1.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_right_lower_shoulder (right_lower_shoulder): { shape: capsule, size: [0, 0, 0.12, 0.06], Q: [0.00705882, -1.33336e-18, 1.47213e-18, -0.707107, 0, -0.707107, 0], contact: -2, rel_includes_mesh_center, }
shape visual (right_upper_elbow): { shape: mesh, size: [1, 1, 1, 1], Q: [0.217587, -2.10593e-05, 0.0125858, -0.707107, 0, -0.707107, 0], mesh: <upper_elbow/E0.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_right_upper_elbow (right_upper_elbow): { shape: capsule, size: [0, 0, 0.107, 0.06], Q: [-0.0472059, -1.33336e-18, -1.05771e-17, -0.707107, 0, -0.707107, 0], contact: -3, rel_includes_mesh_center, }
shape collision_right_lower_shoulder (right_lower_shoulder): { shape: capsule, size: [0, 0, 0.273, 0.06], Q: [7.47116e-13, -7.47017e-13, -0.259559, 3.46251e-12, 0.707107, 0.707107, 5.55112e-17], contact: -2, rel_includes_mesh_center, }
shape visual (right_lower_elbow): { shape: mesh, size: [1, 1, 1, 1], Q: [4.23177e-05, 0.000105171, -0.0200289, -0.707107, 0, -0.707107, 0], mesh: <lower_elbow/E1.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_right_lower_elbow (right_lower_elbow): { shape: capsule, size: [0, 0, 0.1, 0.06], Q: [0.00588235, -1.33336e-18, 1.21091e-18, -0.707107, 0, -0.707107, 0], contact: -2, rel_includes_mesh_center, }
shape visual (right_upper_forearm): { shape: mesh, size: [1, 1, 1, 1], Q: [0.132336, -0.00156713, 0.0374155, -0.707107, 0, -0.707107, 0], mesh: <upper_forearm/W0.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_right_upper_forearm (right_upper_forearm): { shape: capsule, size: [0, 0, 0.088, 0.06], Q: [-0.0388235, -1.33336e-18, -8.71579e-18, -0.707107, 0, -0.707107, 0], contact: -3, rel_includes_mesh_center, }
shape collision_right_lower_elbow (right_lower_elbow): { shape: capsule, size: [0, 0, 0.272, 0.06], Q: [7.44375e-13, -7.44281e-13, -0.24, 3.46251e-12, 0.707107, 0.707107, 5.55112e-17], contact: -10, rel_includes_mesh_center, }
shape visual (right_lower_forearm): { shape: mesh, size: [1, 1, 1, 1], Q: [0.00191909, -0.00263826, -0.0345565, -0.707107, 0, -0.707107, 0], mesh: <lower_forearm/W1.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_right_lower_forearm (right_lower_forearm): { shape: capsule, size: [0, 0, 0.1, 0.06], Q: [0.00588235, -1.33336e-18, 1.21091e-18, -0.707107, 0, -0.707107, 0], contact: -2, rel_includes_mesh_center, }
shape visual (right_wrist): { shape: mesh, size: [1, 1, 1, 1], Q: [0.106397, 0.0019882, -0.0192091, -0.707107, 0, -0.707107, 0], mesh: <wrist/W2.STL>, color: [0.1, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_right_wrist (right_wrist): { shape: capsule, size: [0, 0, 0.165, 0.06], Q: [0.00970588, -1.33336e-18, 2.0599e-18, -0.707107, 0, -0.707107, 0], contact: -3, rel_includes_mesh_center, }
shape collision_right_wrist (right_wrist): { shape: capsule, size: [0, 0, 0.0464, 0.04], Q: [0.0930794, -1.00682e-18, 2.05368e-17, -0.707107, 0, -0.707107, 0], contact: -3, rel_includes_mesh_center, }
shape visual (right_wrist): { shape: capsule, size: [0, 0, 0.01, 0.02], Q: [0.129493, 0.012, -0.03825, -0.5, 0.5, -0.5, 0.5], color: [0, 0, 1, 0.8], rel_includes_mesh_center, }
shape visual (right_wrist): { shape: box, size: [0.005, 0.02, 0.005, 0], Q: [0.14235, -0.020245, -0.032, -0.707107, 0.707107, -1.73112e-12, 1.73128e-12], color: [0, 0, 1, 0.8] }
shape visual (right_wrist): { shape: box, size: [0.01, 0.01, 0.01, 0], Q: [0.09895, 0.000133, -0.00198, -0.707107, 0, -0.707107, 0], color: [0, 0, 0, 1] }
shape visual (left_upper_shoulder): { shape: mesh, size: [1, 1, 1, 1], Q: [0.204968, -0.000259649, -0.0560219, -0.707107, 0, -0.707107, 0], mesh: <upper_shoulder/S0.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_left_upper_shoulder (left_upper_shoulder): { shape: capsule, size: [0, 0, 0.2722, 0.06], Q: [0.152112, -1.33336e-18, 3.36804e-17, -0.707107, 0, -0.707107, 0], contact: -2, rel_includes_mesh_center, }
shape visual (left_lower_shoulder): { shape: mesh, size: [1, 1, 1, 1], Q: [6.04869e-05, -2.01515e-05, -0.0561637, -0.707107, 0, -0.707107, 0], mesh: <lower_shoulder/S1.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_left_lower_shoulder (left_lower_shoulder): { shape: capsule, size: [0, 0, 0.12, 0.06], Q: [0.00705882, -1.33336e-18, 1.47213e-18, -0.707107, 0, -0.707107, 0], contact: -2, rel_includes_mesh_center, }
shape visual (left_upper_elbow): { shape: mesh, size: [1, 1, 1, 1], Q: [0.217587, -2.10593e-05, 0.0125858, -0.707107, 0, -0.707107, 0], mesh: <upper_elbow/E0.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_left_upper_elbow (left_upper_elbow): { shape: capsule, size: [0, 0, 0.107, 0.06], Q: [-0.0472059, -1.33336e-18, -1.05771e-17, -0.707107, 0, -0.707107, 0], contact: -3, rel_includes_mesh_center, }
shape collision_left_lower_shoulder (left_lower_shoulder): { shape: capsule, size: [0, 0, 0.273, 0.06], Q: [7.47116e-13, -7.47017e-13, -0.259559, 3.46251e-12, 0.707107, 0.707107, 5.55112e-17], contact: -2, rel_includes_mesh_center, }
shape visual (left_lower_elbow): { shape: mesh, size: [1, 1, 1, 1], Q: [4.23177e-05, 0.000105171, -0.0200289, -0.707107, 0, -0.707107, 0], mesh: <lower_elbow/E1.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_left_lower_elbow (left_lower_elbow): { shape: capsule, size: [0, 0, 0.1, 0.06], Q: [0.00588235, -1.33336e-18, 1.21091e-18, -0.707107, 0, -0.707107, 0], contact: -2, rel_includes_mesh_center, }
shape visual (left_upper_forearm): { shape: mesh, size: [1, 1, 1, 1], Q: [0.132336, -0.00156713, 0.0374155, -0.707107, 0, -0.707107, 0], mesh: <upper_forearm/W0.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_left_upper_forearm (left_upper_forearm): { shape: capsule, size: [0, 0, 0.088, 0.06], Q: [-0.0388235, -1.33336e-18, -8.71579e-18, -0.707107, 0, -0.707107, 0], contact: -3, rel_includes_mesh_center, }
shape collision_left_lower_elbow (left_lower_elbow): { shape: capsule, size: [0, 0, 0.272, 0.06], Q: [7.44375e-13, -7.44281e-13, -0.24, 3.46251e-12, 0.707107, 0.707107, 5.55112e-17], contact: -2, rel_includes_mesh_center, }
shape visual (left_lower_forearm): { shape: mesh, size: [1, 1, 1, 1], Q: [0.00191909, -0.00263826, -0.0345565, -0.707107, 0, -0.707107, 0], mesh: <lower_forearm/W1.STL>, color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_left_lower_forearm (left_lower_forearm): { shape: capsule, size: [0, 0, 0.1, 0.06], Q: [0.00588235, -1.33336e-18, 1.21091e-18, -0.707107, 0, -0.707107, 0], contact: -2, rel_includes_mesh_center, }
shape visual (left_wrist): { shape: mesh, size: [1, 1, 1, 1], Q: [0.106397, 0.0019882, -0.0192091, -0.707107, 0, -0.707107, 0], mesh: <wrist/W2.STL>, color: [0.1, 0.1, 0.1, 1], rel_includes_mesh_center, }
shape collision_left_wrist (left_wrist): { shape: capsule, size: [0, 0, 0.165, 0.06], Q: [0.00970588, -1.33336e-18, 2.0599e-18, -0.707107, 0, -0.707107, 0], contact: -3, rel_includes_mesh_center, }
shape collision_left_wrist (left_wrist): { shape: capsule, size: [0, 0, 0.0464, 0.04], Q: [0.0930794, -1.00682e-18, 2.05368e-17, -0.707107, 0, -0.707107, 0], contact: -3, rel_includes_mesh_center, }
shape visual (left_wrist): { shape: capsule, size: [0, 0, 0.01, 0.02], Q: [0.129493, 0.012, -0.03825, -0.5, 0.5, -0.5, 0.5], color: [0, 0, 1, 0.8], rel_includes_mesh_center, }
shape visual (left_wrist): { shape: box, size: [0.005, 0.02, 0.005, 0], Q: [0.14235, -0.020245, -0.032, -0.707107, 0.707107, -1.73112e-12, 1.73128e-12], color: [0, 0, 1, 0.8] }
shape visual (left_wrist): { shape: box, size: [0.01, 0.01, 0.01, 0], Q: [0.09895, 0.000133, -0.00198, -0.707107, 0, -0.707107, 0], color: [0, 0, 0, 1] }
shape visual (base): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.026058, 0.000178965, -0.772106, 1, 0, 0, 0], mesh: <base/PEDESTAL.STL>, color: [0.2, 0.2, 0.2, 1], rel_includes_mesh_center, }
shape collision_base (base): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.0426509, -0.000255201, -0.589587, 1, 0, 0, 0], mesh: <base/pedestal_link_collision.STL>, rel_includes_mesh_center, }
shape visual (left_wrist): { shape: mesh, size: [1, 1, 1, 1], Q: [0.139922, -0.000401862, 0.00785846, 0.5, -0.5, -0.5, -0.5], mesh: <electric_gripper/electric_gripper_base.STL>, rel_includes_mesh_center, }
shape collision_left_wrist (left_wrist): { shape: capsule, size: [0, 0, 0.1, 0.029], Q: [0.13855, 0.00588235, 3.06724e-17, 0.5, -0.5, -0.5, -0.5], color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, contact: -2 }
shape visual (l_gripper_l_finger): { shape: mesh, size: [1, 1, 1, 1], Q: [0.00211614, 0.00383573, 0.0286702, 0.707107, -0, 0, 0.707107], mesh: <electric_gripper/fingers/extended_narrow.STL>, rel_includes_mesh_center, }
shape collision_l_gripper_l_finger (l_gripper_l_finger): { shape: box, size: [0.01, 0.0135, 0.1127, 0], Q: [0.01725, 3.83027e-18, 0.0615, 0.707107, -0, 0, 0.707107] }
shape visual (l_gripper_l_finger): { shape: mesh, size: [1, 1, 1, 1], Q: [0.0110665, -6.99422e-05, 0.0992843, -0.707107, 0, 0, -0.707107], mesh: <electric_gripper/fingers/paddle_tip.STL>, rel_includes_mesh_center, }
shape collision_l_gripper_l_finger (l_gripper_l_finger): { shape: box, size: [0.042, 0.0065, 0.037, 0], Q: [0.01275, 2.83107e-18, 0.0977, -0.707107, 0, 0, -0.707107] }
shape visual (l_gripper_r_finger): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.00211614, -0.00383573, 0.0286702, -0.707107, 0, 0, 0.707107], mesh: <electric_gripper/fingers/extended_narrow.STL>, rel_includes_mesh_center, }
shape collision_l_gripper_r_finger (l_gripper_r_finger): { shape: box, size: [0.01, 0.0135, 0.1127, 0], Q: [-0.01725, -3.83027e-18, 0.0615, -0.707107, 0, 0, 0.707107] }
shape visual (l_gripper_r_finger): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.0110665, 6.99422e-05, 0.0992843, -0.707107, 0, 0, 0.707107], mesh: <electric_gripper/fingers/paddle_tip.STL>, rel_includes_mesh_center, }
shape collision_l_gripper_r_finger (l_gripper_r_finger): { shape: box, size: [0.042, 0.0065, 0.037, 0], Q: [-0.01275, -2.83107e-18, 0.0977, -0.707107, 0, 0, 0.707107] }
shape visual (right_wrist): { shape: mesh, size: [1, 1, 1, 1], Q: [0.139922, -0.000401862, 0.00785846, 0.5, -0.5, -0.5, -0.5], mesh: <electric_gripper/electric_gripper_base.STL>, rel_includes_mesh_center, }
shape collision_right_wrist (right_wrist): { shape: capsule, size: [0, 0, 0.1, 0.029], Q: [0.13855, 0.00588235, 3.06724e-17, 0.5, -0.5, -0.5, -0.5], color: [0.5, 0.1, 0.1, 1], rel_includes_mesh_center, contact: -2 }
shape visual (r_gripper_l_finger): { shape: mesh, size: [1, 1, 1, 1], Q: [0.00211614, 0.00383573, 0.0286702, 0.707107, -0, 0, 0.707107], mesh: <electric_gripper/fingers/extended_narrow.STL>, rel_includes_mesh_center, }
shape collision_r_gripper_l_finger (r_gripper_l_finger): { shape: box, size: [0.01, 0.0135, 0.1127, 0], Q: [0.01725, 3.83027e-18, 0.0615, 0.707107, -0, 0, 0.707107] }
shape visual (r_gripper_l_finger): { shape: mesh, size: [1, 1, 1, 1], Q: [0.0119087, 0.0002756, 0.0933624, -0.707107, 0, 0, -0.707107], mesh: <electric_gripper/fingers/half_round_tip.STL>, rel_includes_mesh_center, }
shape collision_r_gripper_l_finger (r_gripper_l_finger): { shape: capsule, size: [0, 0, 0.037, 0.008], Q: [0.01275, 2.83915e-18, 0.0998765, -0.707107, 0, 0, -0.707107], rel_includes_mesh_center, }
shape visual (r_gripper_r_finger): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.00211614, -0.00383573, 0.0286702, -0.707107, 0, 0, 0.707107], mesh: <electric_gripper/fingers/extended_narrow.STL>, rel_includes_mesh_center, }
shape collision_r_gripper_r_finger (r_gripper_r_finger): { shape: box, size: [0.01, 0.0135, 0.1127, 0], Q: [-0.01725, -3.83027e-18, 0.0615, -0.707107, 0, 0, 0.707107] }
shape visual (r_gripper_r_finger): { shape: mesh, size: [1, 1, 1, 1], Q: [-0.0119087, -0.0002756, 0.0933624, -0.707107, 0, 0, 0.707107], mesh: <electric_gripper/fingers/half_round_tip.STL>, rel_includes_mesh_center, }
shape collision_r_gripper_r_finger (r_gripper_r_finger): { shape: capsule, size: [0, 0, 0.037, 0.008], Q: [-0.01275, -2.83915e-18, 0.0998765, -0.707107, 0, 0, 0.707107], rel_includes_mesh_center, }

joint head_pan (base head): { joint: hingeX, from: [0.06, 0, 0.686, 0.707107, 0, -0.707107, 0], limits: [-1.3963, 1.3963], ctrl_limits: [10000, 50000, 1] }
joint right_s0 (base right_upper_shoulder): { joint: hingeX, from: [0.0640272, -0.259027, 0.129626, 0.653281, -0.270599, -0.653281, -0.270599], limits: [-1.70168, 1.70168], ctrl_limits: [1.5, 50, 1] }
joint left_s0 (base left_upper_shoulder): { joint: hingeX, from: [0.0640272, 0.259027, 0.129626, 0.653281, 0.270599, -0.653281, 0.270599], limits: [-1.70168, 1.70168], ctrl_limits: [1.5, 50, 1] }
joint right_s1 (right_upper_shoulder right_lower_shoulder): { joint: hingeX, from: [0.27035, 0, -0.069, -0.707107, 1.11022e-16, -5.55112e-17, -0.707107], limits: [-2.147, 1.047], ctrl_limits: [1.5, 50, 1] }
joint left_s1 (left_upper_shoulder left_lower_shoulder): { joint: hingeX, from: [0.27035, 0, -0.069, -0.707107, 1.11022e-16, -5.55112e-17, -0.707107], limits: [-2.147, 1.047], ctrl_limits: [1.5, 50, 1] }
joint right_e0 (right_lower_shoulder right_upper_elbow): { joint: hingeX, from: [2.26485e-17, 0, -0.102, -0.5, -0.5, -0.5, 0.5], limits: [-3.05418, 3.05418], ctrl_limits: [1.5, 50, 1] }
joint left_e0 (left_lower_shoulder left_upper_elbow): { joint: hingeX, from: [2.26485e-17, 0, -0.102, -0.5, -0.5, -0.5, 0.5], limits: [-3.05418, 3.05418], ctrl_limits: [1.5, 50, 1] }
joint right_e1 (right_upper_elbow right_lower_elbow): { joint: hingeX, from: [0.26242, 0, -0.069, -0.5, 0.5, 0.5, -0.5], limits: [-0.05, 2.618], ctrl_limits: [1.5, 50, 1] }
joint left_e1 (left_upper_elbow left_lower_elbow): { joint: hingeX, from: [0.26242, 0, -0.069, -0.5, 0.5, 0.5, -0.5], limits: [-0.05, 2.618], ctrl_limits: [1.5, 50, 1] }
joint right_w0 (right_lower_elbow right_upper_forearm): { joint: hingeX, from: [2.30016e-17, 0, -0.10359, -0.5, -0.5, -0.5, 0.5], limits: [-3.059, 3.059], ctrl_limits: [4, 15, 1] }
joint left_w0 (left_lower_elbow left_upper_forearm): { joint: hingeX, from: [2.30016e-17, 0, -0.10359, -0.5, -0.5, -0.5, 0.5], limits: [-3.059, 3.059], ctrl_limits: [4, 15, 1] }
joint right_w1 (right_upper_forearm right_lower_forearm): { joint: hingeX, from: [0.2707, 0, -0.01, -0.5, 0.5, 0.5, -0.5], limits: [-1.5708, 2.094], ctrl_limits: [4, 15, 1] }
joint left_w1 (left_upper_forearm left_lower_forearm): { joint: hingeX, from: [0.2707, 0, -0.01, -0.5, 0.5, 0.5, -0.5], limits: [-1.5708, 2.094], ctrl_limits: [4, 15, 1] }
joint right_w2 (right_lower_forearm right_wrist): { joint: hingeX, from: [2.57516e-17, 0, -0.115975, -0.5, -0.5, -0.5, 0.5], limits: [-3.059, 3.059], ctrl_limits: [4, 15, 1] }
joint left_w2 (left_lower_forearm left_wrist): { joint: hingeX, from: [2.57516e-17, 0, -0.115975, -0.5, -0.5, -0.5, 0.5], limits: [-3.059, 3.059], ctrl_limits: [4, 15, 1] }
joint r_gripper_l_finger_joint (right_wrist r_gripper_l_finger): { joint: transX, from: [0.15855, -0.0015, 3.52052e-17, -0.5, -0.5, -0.5, -0.5], limits: [0, 0.020833], ctrl_limits: [5, 20, 1], r_gripper }
joint r_gripper_r_finger_joint (right_wrist r_gripper_r_finger): { joint: transX, from: "t(0.15855 0.0015 0) d(90 1 0 0) d(-90 0 1 0) ", to: "d(-180 0 1 0)", mimic: "r_gripper_l_finger_joint", limits: [-0.020833, 0], ctrl_limits: [5, 20, 1], r_gripper }
joint l_gripper_l_finger_joint (left_wrist l_gripper_l_finger): { joint: transX, from: [0.15855, -0.0015, 3.52052e-17, -0.5, -0.5, -0.5, -0.5], limits: [0, 0.020833], ctrl_limits: [5, 20, 1], l_gripper }
joint l_gripper_r_finger_joint (left_wrist l_gripper_r_finger): { joint: transX, from: "t(0.15855 0.0015 0) d(90 1 0 0) d(-90 0 1 0) ", to: "d(-180 0 1 0)", mimic: "l_gripper_l_finger_joint", limits: [-0.020833, 0], ctrl_limits: [5, 20, 1], l_gripper}
