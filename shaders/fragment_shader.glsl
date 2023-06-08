#version 330 core

out vec4 FragColor;

void main()
{
    // Get the normalized device coordinates (NDC) of the fragment
    vec2 ndc = gl_FragCoord.xy / vec2(800.0, 600.0);

    // Use the NDC values to set the RGB color components
    vec3 color = vec3(ndc.x, ndc.y, 0.5);

    // Set the alpha value to 1.0 (fully opaque)
    float alpha = 1.0;

    // Set the final fragment color
    FragColor = vec4(color, alpha);
}
