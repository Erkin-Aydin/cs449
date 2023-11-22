#include "Line.h"

namespace ORCA {
    
    Line::Line() {
        point = Vector(0, 0);
        direction = Vector(1, 0);
    }

    Line::Line(Vector point, Vector direction) {
        this->point = point;
        this->direction = direction;
    }
}