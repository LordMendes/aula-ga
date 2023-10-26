<script setup lang="ts">
import { ref, defineProps } from "vue";

const hexValues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"];
let hex = "#";
for (let i = 0; i < 6; i++) {
  const index = Math.floor(Math.random() * hexValues.length);
  hex += hexValues[index];
}

const props = defineProps({
  fill: {
    default: null,
  },
  showFitnessScore: {
    default: false,
  },
  size: {
    default: 50,
  },
});

const fillColor = ref(props.fill ? props.fill : hex);
const size = ref(props.size ? props.size : 50);

// Function to calculate fitness score
const calculateFitnessScore = (color) => {
  // Convert hex color to RGB
  const r = parseInt(color.substring(1, 3), 16);
  const g = parseInt(color.substring(3, 5), 16);
  const b = parseInt(color.substring(5, 7), 16);

  // Calculate Euclidean distance
  const distance = Math.sqrt((r - 0) ** 2 + (g - 255) ** 2 + (b - 0) ** 2);

  // Fitness score formula (adjust this based on desired range and scale)
  const maxDistance = Math.sqrt(255 ** 2 + 255 ** 2 + 255 ** 2);
  const fitness = 1 - distance / maxDistance;

  return fitness;
};

// Calculate fitness score based on the initial fill color
const fitnessScore = calculateFitnessScore(fillColor.value).toPrecision(2);
</script>

<template>
  <div class="flex flex-col justify-center items-center">
    <span v-if="showFitnessScore">{{ fitnessScore }}</span>
    <svg
      version="1.0"
      xmlns="http://www.w3.org/2000/svg"
      width="400.000000pt"
      viewBox="0 0 527.000000 474.000000"
      preserveAspectRatio="xMidYMid meet"
      :height="size"
    >
      <g
        transform="translate(0.000000,474.000000) scale(0.100000,-0.100000)"
        :fill="fillColor"
        stroke="none"
      >
        <path
          d="M1753 4376 c-55 -25 -75 -69 -70 -153 8 -135 89 -253 215 -311 45
-20 77 -27 150 -30 91 -4 93 -5 86 -26 -4 -11 -9 -160 -11 -331 l-4 -309 -77
-81 c-42 -44 -95 -108 -117 -142 -22 -35 -42 -62 -45 -60 -159 80 -316 160
-318 162 -2 2 -25 148 -51 324 -32 212 -53 327 -63 338 -189 223 -443 503
-459 508 -29 9 -73 -24 -77 -58 -3 -27 -6 -24 271 -340 88 -101 158 -190 161
-205 3 -15 26 -163 50 -330 25 -167 50 -310 57 -319 7 -8 94 -55 192 -105 143
-71 178 -93 174 -106 -3 -9 -20 -59 -37 -109 l-32 -93 -37 0 c-20 0 -109 5
-199 10 -89 6 -169 7 -176 3 -8 -4 -136 -124 -285 -266 -193 -183 -277 -256
-289 -253 -38 12 -486 116 -499 116 -21 0 -53 -38 -53 -63 0 -50 16 -56 295
-123 147 -35 282 -64 298 -64 23 0 47 17 116 83 47 46 172 165 277 265 l192
182 163 -10 c90 -6 165 -13 166 -14 2 -2 -1 -55 -7 -118 -14 -161 4 -343 50
-503 11 -38 20 -73 20 -76 0 -4 -76 -57 -170 -118 -164 -107 -170 -112 -170
-144 0 -19 32 -208 70 -421 39 -212 70 -394 70 -404 0 -10 -64 -68 -155 -140
-100 -80 -157 -132 -161 -148 -10 -37 20 -74 59 -74 26 0 64 25 207 140 96 77
179 148 183 158 6 12 -16 159 -62 413 -39 217 -73 404 -76 416 -5 20 12 34
125 109 72 48 131 85 133 83 2 -2 23 -38 47 -79 80 -138 200 -272 313 -349 66
-45 180 -97 257 -118 101 -28 302 -25 400 6 234 73 451 258 566 484 13 26 29
47 34 47 6 0 65 -36 130 -80 104 -69 120 -84 115 -103 -3 -12 -37 -197 -76
-412 -48 -265 -68 -397 -62 -413 4 -12 87 -86 183 -162 143 -115 181 -140 207
-140 39 0 69 37 59 74 -4 16 -61 68 -161 148 -97 77 -155 130 -155 141 0 10
32 191 70 402 39 211 70 400 70 420 0 35 -2 37 -162 142 -90 58 -165 107 -167
109 -2 2 8 45 22 96 14 51 31 127 38 168 14 83 17 328 6 402 l-8 46 93 6 c51
4 125 8 164 9 l70 2 277 -262 c229 -218 281 -263 305 -263 16 0 150 29 297 64
279 67 295 73 295 123 0 26 -32 63 -55 63 -8 0 -127 -27 -265 -60 l-251 -60
-270 258 c-149 141 -277 261 -285 265 -8 4 -85 3 -171 -3 -87 -5 -173 -10
-193 -10 l-35 0 -38 111 c-21 61 -37 112 -35 114 2 1 80 41 173 88 94 47 177
92 184 100 7 9 32 152 57 319 24 167 47 315 50 330 3 15 73 104 161 205 277
316 274 313 271 340 -4 34 -48 67 -77 58 -16 -5 -270 -285 -459 -508 -10 -11
-31 -126 -63 -338 -26 -176 -49 -322 -51 -324 -1 -1 -73 -38 -158 -80 l-154
-77 -16 23 c-45 69 -107 143 -179 213 l-81 78 0 283 c0 155 -3 297 -6 314 l-6
31 70 0 c208 0 368 138 388 337 10 94 -37 161 -118 170 -80 8 -139 -45 -153
-139 -3 -21 -17 -50 -30 -65 l-23 -28 -612 -3 -612 -2 -34 34 c-24 24 -34 43
-34 65 0 99 -107 168 -197 127z"
        />
      </g>
    </svg>
  </div>
</template>
