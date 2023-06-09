import { Deta } from "deta";
import { env } from '$env/dynamic/private';

const blackholeKey = env.BLACKHOLE_DATA_KEY ? env.BLACKHOLE_DATA_KEY : null;

const detaBh = Deta(blackholeKey || "backup");
export const inputPics = detaBh.Base(
    "black-hole"
)

const deta = Deta(env.DETA_PROJECT_KEY || "backup");
export const picData = deta.Base(
    "blackhole_pics"
)

export const baseUrl = env.BLACKHOLE_URL ? env.BLACKHOLE_URL + "api" : "NO_BLACKHOLE";