#ifndef ORCA_LINE_H
#define ORCA_LINE_H

#include "Vector.h"

namespace ORCA {
    
    /**
     * @brief a line with direction. that is it. nothing more.
    */
    class Line {
        
        public:
        
        /**
         * @brief any point that the line intercepts in 2d space
        */
        Vector point;

        /**
         * @brief direction of the line in 2d space
        */
        Vector direction;

        public:

        /**
         * @brief constructor for a directed line. by default, the point is (0, 0) and the direction is (1, 0)
        */
        Line();

        /**
         * @brief initializer constructor for a directed line
         * @param[in] point any point that the line intercepts in 2d space
         * @param[in] direction direction of the line in 2d space
        */
       Line(Vector point, Vector direction);
    };
}

#endif //ORCA_LINE_H