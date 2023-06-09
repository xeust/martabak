<script>
	export let data;
</script>


<div class="app-container">
    <h1>wumblr</h1>
    <div class="img-column-container">
        {#each data.pics as pic}
        <div class="img-container">
            <img style="width: 100%;" src="{pic.url}" alt="thumbnail"/>
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
    width: 400px;
}

.img-container {
    display: flex;
    position: relative;
    width: 400px;
    margin-bottom: 1em;
}
</style>