<script>
	export let data;

    async function publish(picUrl, baseUrl) {
        try {
            const response = await fetch('/api/publish', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    type: 'blackhole_pic',
                    url: `${baseUrl + picUrl}`,
                }),
            });

            if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error making POST request:', error);
        }
	}
</script>


<div class="app-container">
    <h1>wumblr admin</h1>
    <div class="img-column-container">
        {#each data.pics as pic}
        <div class="img-container">
            <img style="width: 100%;" src="{data.baseUrl + pic.thumbnail}" alt="thumbnail"/>
            <button class="img-publish" on:click={() => publish(pic.url, data.baseUrl)}>publish</button>
        </div>
        {/each}
    </div>
</div>

<style>
.app-container{
    display: flex;
    flex-direction: column;
    align-items: center;
}

.img-column-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 300px;
}

.img-container {
    display: flex;
    position: relative;
    width: 300px;
    margin-bottom: 1em;
}

.img-publish {
    position: absolute;
    top: 10px;
    right: 10px;
    width: 60px;
    height: 30px;
}
</style>