const WIDTH = 20;
const HEIGHT = 1;

const vertexCount = 6;
const vertexLocations = [
  // X, Y
  -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0, 1.0,
  //   -100.0, -100.0, 100.0, -100.0, -100.0, 200.0,
];

function bytes_to_int(r, g, b, a) {
  return ((r * 256 + g) * 256 + b) * 256 + a;
}

function make_viewport_rect(gl) {
  //make full-viewport rect
  var triangleArray = gl.createVertexArray();
  gl.bindVertexArray(triangleArray);

  const buffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
  gl.bufferData(
    gl.ARRAY_BUFFER,
    new Float32Array(vertexLocations),
    gl.STATIC_DRAW
  );
  gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
  gl.enableVertexAttribArray(0);
}

function make_shader(gl, frag_code) {
  var vertexShader = gl.createShader(gl.VERTEX_SHADER);

  gl.shaderSource(
    vertexShader,
    `#version 300 es
    layout(location=0) in vec2 a_position;
    out vec3 vPosition;
    void main() {
        vPosition = vec3(a_position, 0.0);
        gl_Position = vec4(a_position, 0.0, 1.0);
    }
      `
  );
  gl.compileShader(vertexShader);

  if (!gl.getShaderParameter(vertexShader, gl.COMPILE_STATUS)) {
    console.error(gl.getShaderInfoLog(vertexShader));
  }

  var fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
  gl.shaderSource(fragmentShader, frag_code);
  gl.compileShader(fragmentShader);

  if (!gl.getShaderParameter(fragmentShader, gl.COMPILE_STATUS)) {
    console.error(gl.getShaderInfoLog(fragmentShader));
  }

  var program = gl.createProgram();
  gl.attachShader(program, vertexShader);
  gl.attachShader(program, fragmentShader);
  gl.linkProgram(program);

  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    console.error(gl.getProgramInfoLog(program));
  }

  gl.useProgram(program);

  return program;
}

function add_attribute_pointer(gl, program) {
  const positionLocation = gl.getAttribLocation(program, "a_position");
  gl.enableVertexAttribArray(positionLocation);
  const fieldCount = vertexLocations.length / vertexCount;
  gl.vertexAttribPointer(
    positionLocation,
    fieldCount,
    gl.FLOAT,
    gl.FALSE,
    fieldCount * Float32Array.BYTES_PER_ELEMENT,
    0
  );
}

function load_texture(gl, glsl_name, glsl_num, tex_id, img_src, program) {
  gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
  gl.pixelStorei(gl.UNPACK_COLORSPACE_CONVERSION_WEBGL, false);
  return new Promise((resolve, reject) => {
    // const samplerId = gl.getUniformLocation(program, "uSampler");
    const samplerId = gl.getUniformLocation(program, glsl_name);
    gl.activeTexture(tex_id);
    var tex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.texImage2D(
      gl.TEXTURE_2D,
      0,
      gl.RGBA,
      1,
      1,
      0,
      gl.RGBA,
      gl.UNSIGNED_BYTE,
      new Uint8Array([255, 0, 0, 255])
    ); //temporary texture buffer
    gl.uniform1i(samplerId, glsl_num);

    var img = new Image();
    img.src = img_src;
    img.onload = function () {
      console.log(img_src, img.width, img.height);
      gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, img); //repopulate buffer
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);

      //  set height
      gl.uniform1i(
        gl.getUniformLocation(program, glsl_name + "_height"),
        img.height
      );

      resolve();
    };
  });
}

function setupGlitter(frag_code) {
  const canvas = document.getElementById("canvasGlitter");
  canvas.width = WIDTH; //set concrete dimensions
  canvas.height = HEIGHT;

  const gl = canvas.getContext("webgl2");
  gl.viewport(0, 0, WIDTH, HEIGHT);

  //make shader program
  const program = make_shader(gl, frag_code);

  // Add attribute pointer to our vertex locations
  //   add_attribute_pointer(gl, program);
  make_viewport_rect(gl);

  //get uniform pointers
  gl.uniform1f(gl.getUniformLocation(program, "SEEDS_WIDTH"), WIDTH);
  gl.clearColor(1.0, 1.0, 0.5, 0);

  //render loop
  const render = (timestamp) => {
    gl.clear(gl.COLOR_BUFFER_BIT);

    gl.useProgram(program);

    gl.drawArrays(gl.TRIANGLES, 0, vertexCount);
    // window.requestAnimationFrame(render);

    var pixels = new Uint8Array(
      4 * gl.drawingBufferWidth * gl.drawingBufferHeight
    );
    gl.readPixels(
      0,
      0,
      gl.drawingBufferWidth,
      gl.drawingBufferHeight,
      gl.RGBA,
      gl.UNSIGNED_BYTE,
      pixels
    );
    const allowed_nums = [
      629551616, 310303897, 265998072, 58091853, 3217788227, 563748665,
      2286940694, 820803307, 1966060902, 108698829, 190045874, 3206262,
      4045963015, 223661537, 1544688274, 293696584, 1038807941, 31756878,
      1224711373, 133647424,
    ];
    var smallest_num = Number.MAX_SAFE_INTEGER;
    for (var i = 0; i < pixels.length; i += 4) {
      const expected_num = allowed_nums[i / 4];

      const n = bytes_to_int(
        pixels[i],
        pixels[i + 1],
        pixels[i + 2],
        pixels[i + 3]
      );
      if (n != expected_num) {
        console.error("bad num " + i / 4 + "/" + allowed_nums.length);
        console.log("EXP: " + expected_num.toString(16).padStart(8, "0"));
        console.log(
          "GOT: " +
            pixels[i].toString(16).padStart(2, "0") +
            pixels[i + 1].toString(16).padStart(2, "0") +
            pixels[i + 2].toString(16).padStart(2, "0") +
            pixels[i + 3].toString(16).padStart(2, "0")
        );
      } else console.log(n);
      if (n < smallest_num) {
        smallest_num = n;
      }
    }
    console.log("smallest num", smallest_num);
    // window.requestAnimationFrame(render);
  };

  //Load noise texture (kinda important)
  Promise.allSettled([
    load_texture(gl, "seeds_tex", 0, gl.TEXTURE0, "seeds.png", program),
    load_texture(gl, "map_1", 1, gl.TEXTURE1, "map_1.png", program),
    load_texture(gl, "map_2", 2, gl.TEXTURE2, "map_2.png", program),
    load_texture(gl, "map_3", 3, gl.TEXTURE3, "map_3.png", program),
    load_texture(gl, "map_4", 4, gl.TEXTURE4, "map_4.png", program),
    load_texture(gl, "map_5", 5, gl.TEXTURE5, "map_5.png", program),
    load_texture(gl, "map_6", 6, gl.TEXTURE6, "map_6.png", program),
    load_texture(gl, "map_7", 7, gl.TEXTURE7, "map_7.png", program),
  ]).then(() => {
    window.requestAnimationFrame(render);
  });
}

const xhttp = new XMLHttpRequest();
xhttp.onload = function () {
  const frag_code = this.responseText;
  setupGlitter(frag_code);
};
xhttp.open("GET", "day5.glsl", true);
xhttp.send();
