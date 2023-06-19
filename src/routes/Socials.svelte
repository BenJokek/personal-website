<script>
    let socialLinks = [
        {
            name: "LinkedIn",
            icon: "fa-linkedin",
            url: "https://www.linkedin.com/in/benjamin-zambelli/",
        },
        {
            name: "GitHub",
            icon: "fa-square-github",
            url: "https://github.com/BenJokek",
        },
        {
            name: "YouTube",
            icon: "fa-youtube",
            url: "https://www.youtube.com/channel/UCHAtb9BayfnlFDCGXKMiysA",
        },
    ];
</script>

<ul>
    {#each socialLinks as link}
        <li>
            <a href={link.url} target="_blank">
                <i
                    class={"fa-brands " + link.icon + " fa-2xl"}
                    style="color: #ffffff;"
                /><br />
                <span class="socials">{link.name}</span>
            </a>
        </li>
    {/each}
</ul>

<style>
    ul {
        list-style: none;
        margin: 20px;
        margin-bottom: 0px;
        display: flex;
    }
    li {
        text-align: center;
    }

    .socials {
        padding: 20px;
    }
    .fa-brands {
        padding: 25px;
    }
</style>
