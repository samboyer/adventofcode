#version 300 es

precision highp float;
precision highp int;

uniform float SEEDS_WIDTH;
const int MAX_MAP_HEIGHT = 50;


uniform sampler2D seeds_tex;

uniform sampler2D map_1;
uniform sampler2D map_2;
uniform sampler2D map_3;
uniform sampler2D map_4;
uniform sampler2D map_5;
uniform sampler2D map_6;
uniform sampler2D map_7;

uniform int map_1_height;
uniform int map_2_height;
uniform int map_3_height;
uniform int map_4_height;
uniform int map_5_height;
uniform int map_6_height;
uniform int map_7_height;


// highp float vec4ToUint(vec4 v) {
//     return (v.a * 255.0) + (v.b * (65536.0-255.0)) + (v.g * (16777216.0-65535.0)) + (v.r * (4294967295.0-16777215.0));
// }

uint vec4ToUint2(vec4 v) {
    return uint(v.a * 255.0) + uint(v.b*255.0) * (256u) + uint(v.g * 255.0) * (256u*256u) + uint(v.r * 255.0) * (256u*256u*256u);
}

uint better_mod(uint x,uint modulo)
{
    return x - modulo * (x / modulo);
}

vec4 uintToVec42(uint i){
    // i= 0x0bfcb8d43u;
    float a = float(better_mod(i, 0x100u));
    float b = float(better_mod(i/256u, 0x100u));
    float g = float(better_mod(i/65536u, 0x100u));
    float r = float(better_mod(i/16777216u, 0x100u));
    return vec4(r/255.0, g/255.0, b/255.0, a/255.0);
}

// vec4 uintToVec4(highp float i){
//     float a = mod(i, 256.0);
//     float b = mod(floor(i/256.0), 256.0);
//     float g = mod(floor(i/65536.0), 256.0);
//     float r = mod(floor(i/16777216.0), 256.0);
//     return vec4(r/255.0, g/255.0, b/255.0, a/255.0);
// }




uint lookup_map(sampler2D map, uint current_pixel_num, int map_height){
    float map_height_f = float(map_height);
    for (int i=0; i<MAX_MAP_HEIGHT; i++){
        float y = float(i)/map_height_f;
        if (y>=1.0){break;}
        vec4 dest_col = texture(
            map,
            vec2(
                0.0/3.0,
                float(i)/map_height_f
            )
        );
        vec4 source_col = texture(
            map,
            vec2(
                1.0/3.0,
                float(i)/map_height_f
            )
        );
        vec4 length = texture(
            map,
            vec2(
                2.0/3.0,
                float(i)/map_height_f
            )
        );
        uint dest_num = vec4ToUint2(dest_col);
        uint source_num = vec4ToUint2(source_col);
        uint length_num = vec4ToUint2(length);

        if(current_pixel_num >= source_num && current_pixel_num < (source_num + length_num)){
            current_pixel_num = dest_num + (current_pixel_num - source_num);
            break;
        }
    }

    return current_pixel_num;
}


in vec3 vPosition;
out vec4 fragColor;

void main() {

    vec2 pos = vPosition.xy+vec2(1,0.0); // is in pixels

    vec4 frag_color = texture(
        seeds_tex,
        pos/2.0 //is in 0-1
    );

    // fragColor = frag_color;

    uint current_pixel_num = vec4ToUint2(frag_color);

    current_pixel_num = lookup_map(map_1, current_pixel_num, map_1_height);
    current_pixel_num = lookup_map(map_2, current_pixel_num, map_2_height);
    current_pixel_num = lookup_map(map_3, current_pixel_num, map_3_height);
    current_pixel_num = lookup_map(map_4, current_pixel_num, map_4_height);
    current_pixel_num = lookup_map(map_5, current_pixel_num, map_5_height);
    current_pixel_num = lookup_map(map_6, current_pixel_num, map_6_height);
    current_pixel_num = lookup_map(map_7, current_pixel_num, map_7_height);
    fragColor = uintToVec42(current_pixel_num);
}

