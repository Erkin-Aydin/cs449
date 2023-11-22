#include "Vector.h"

#include <cmath>
#include <iostream>

namespace ORCA {
    const float EPSILON = 0.00001f;

    Vector::Vector() {

    }
    Vector::Vector(const float x, const float y) {
        x_ = x;
        y_ = y;
    }
    float Vector::x() const {
        return x_;
    }
    float Vector::y() const {
        return y_;
    }
    float Vector::length() const {
        return std::sqrt(x_ * x_ + y_ * y_);
    }
    Vector Vector::operator-() const {
        return Vector(-x_, -y_);
    }
    Vector Vector::operator+(const Vector& other) const {
        return Vector(x_ + other.x_, y_ + other.y_);
    }
    Vector Vector::operator-(const Vector& other) const {
        return Vector(x_ - other.x_, y_ - other.y_);
    }
    Vector Vector::operator*(const float scalar) const {
        return Vector(x_ * scalar, y_ * scalar);
    }
    Vector Vector::operator/(const float scalar) const {
        if(scalar == 0.0f)
            std::cout << "Division by zero encountered!" << std::endl;
            return Vector(0.0f, 0.0f);
        return Vector(x_ / scalar, y_ / scalar);
    }
    Vector& Vector::operator+=(const Vector& other) {
        x_ += other.x_;
        y_ += other.y_;
        return *this;
    }
    Vector& Vector::operator-=(const Vector& other) {
        x_ -= other.x_;
        y_ -= other.y_;
        return *this;
    }
    Vector& Vector::operator*=(const float scalar) {
        x_ *= scalar;
        y_ *= scalar;
        return *this;
    }
    Vector& Vector::operator/=(const float scalar) {
        if(scalar == 0.0f) {
            std::cout << "Division by zero encountered! x and y values will be set to 0.0f ." << std::endl;
            x_ = 0.0f;
            y_ = 0.0f;
            return *this;
        }
        x_ /= scalar;
        y_ /= scalar;
        return *this;
    }
    Vector Vector::operator+() const {
        return *this;
    }
    bool Vector::operator==(const Vector& other) const {
        return false; // TODO 
    }
    bool Vector::operator!=(const Vector& other) const {
        return false; // TODO
    }
} // namespace ORCA