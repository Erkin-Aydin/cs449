#ifndef ORCA_VECTOR_H
#define ORCA_VECTOR_H

#include <cmath>
#include <ostream>

namespace ORCA {

    extern const float EPSILON;

    class Vector {

    private:
        float x_;
        float y_;

    public:

        /**
         * @brief     constructor for 2d zero vector
        */
        Vector();

        /**
         * @brief     initializer constructor for 2d vector
         * @param[in] x x coordinate for 2d vector.
         * @param[in] y y coordinate for 2d vector.
        */
        Vector(const float x, const float y);

        /**
         * @brief   computes x coordinate of the vector
         * @return  x coordinate of the vector
        */
        float x() const;

        /**
         * @brief   computes y coordinate of the vector
         * @return  y coordinate of the vector
        */
        float y() const;

        /**
         * @brief   computes length of the vestor in 2d space
         * @return  length of the vestor in 2d space
        */
        float length() const;

        /**
         * @brief computes the negation (negative) of the vector.
         * @return negation (negative) of the vector.
        */
        Vector operator-() const;

        /**
         * @brief   Returns the vector. Might be necessary in computation, hence added.
         * @return  vector itself.
        */
        Vector operator+() const;

        /**
         * @brief   computes the sum of two 2d vectors.
         * @return  sum of two 2d vectors.
        */
        Vector operator+(const Vector& other) const;

        /**
         * @brief   computes the difference of two 2d vectors.
         * @return  difference of two 2d vectors.
        */
        Vector operator-(const Vector& other) const;

        /**
         * @brief   computes the scalar multiplication of the vector with the parameter scalar.
         * @param[in] scalar the scalar value to multiply the vector
         * @return  scalar multiplication of the vector with the parameter scalar.
        */
        Vector operator*(const float scalar) const;

        /**
         * @brief   computes the scalar division of the vector with the parameter scalar.
         * @param[in] scalar the scalar value to divide the vector
         * @return  scalar division of the vector with the parameter scalar.
        */
        Vector operator/(const float scalar) const;

        /**
         * @brief   computes the sum of this vector with the parameter other vector, and updates its value with the computed one.
         * @param[in] other the vector to sum this vector
         * @return  the updated vector.
        */
        Vector& operator+=(const Vector& other);
        
        /**
         * @brief   computes the difference of this vector with the parameter other vector, and updates its value with the computed one.
         * @param[in] other the vector to subtract from this vector
         * @return  the updated vector.
        */
        Vector& operator-=(const Vector& other);

        /**
         * @brief   computes the scalar multiplication of this vector with the parameter scalar.
         * @param[in] scalar the scalar value to multiply the vector
         * @return  this vector scalar multiplied.
        */
        Vector& operator*=(const float scalar);

        /**
         * @brief   computes the scalar division of this vector with the parameter scalar.
         * @param[in] scalar the scalar value to divide the vector
         * @return  this vector scalar divided.
        */
        Vector& operator/=(const float scalar);

        /**
         * @brief   checks whether this vector is equal to the parameter vector by value
         * @param[in] other the vector to compare this vector with
         * @return  true if two are equal by value, false if not.
        */
        bool operator==(const Vector& other) const;

        /**
         * @brief   checks whether this vector is not equal to the parameter vector by value
         * @param[in] other the vector to compare this vector with
         * @return  true if two are not equal by value, false if they are.
        */
        bool operator!=(const Vector& other) const;
    };
    
}

#endif // VECTOR_H
