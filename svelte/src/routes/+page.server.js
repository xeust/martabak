import { picData, baseUrl } from "$lib/server/deta";

export async function load() {
    console.log(picData);
    const {items: picsList} = await picData.fetch({});
	return {
		pics: picsList,
        baseUrl
	};
}