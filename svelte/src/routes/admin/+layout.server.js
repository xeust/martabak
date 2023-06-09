import { inputPics, baseUrl } from "$lib/server/deta";

export async function load() {
    const {items: picsList} = await inputPics.fetch({});
	return {
		pics: picsList,
        baseUrl
	};
}