<script>
    export let title = "Project";
    export let description = "Description";
    export let images;
    export let date;
    export let project_link;
    export let skills;
</script>

<svelte:head>
    <title>{title}</title>
    <meta name="description" content={description} />
</svelte:head>

<div>
    <h1>
        {title}
    </h1>
    {#each images as image}
        <img src={image} alt="project related content" />
    {/each}

    <p>{date}</p>
    <slot />
    <a href={project_link} target="_blank">See Project</a>
    <h2>
        Skills: {#each skills as skill, index}
            {index > 0 ? " · " : ""}
            {skill}
        {/each}
    </h2>
</div>

<style>
    div {
        color: #333;
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    h1 {
        color: #ffffff;
        font-size: 24px;
        margin-bottom: 10px;
    }

    p {
        color: #cfcdcd;
        font-size: 16px;
        margin-bottom: 15px;
        line-height: 1.5;
    }

    a {
        color: #0088cc;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    h2 {
        color: #ffffff;
        font-size: 18px;
        font-weight: normal;
        margin-bottom: 20px;
    }
    img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
</style>
