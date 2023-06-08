#version 330 core

uniform float rotation_angle;  // Angle of rotation in degrees

layout (location = 0) in vec4 vPosition;

mat2 rotation_matrix(float angle) {
    float c = cos(angle);
    float s = sin(angle);
    return mat2(c, -s, s, c);
}

void main()
{
    // Convert the rotation angle from degrees to radians
    float angle_rad = radians(rotation_angle);

    // Calculate the rotation matrix
    mat2 rotation = rotation_matrix(angle_rad);

    // Apply the rotation transformation to the vertex position
    vec2 rotated_position = rotation * vPosition.xy;
    gl_Position = vec4(rotated_position, vPosition.zw);
}
