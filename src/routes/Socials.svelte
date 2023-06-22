<script>
    let socialLinks = [
        {
            name: "LinkedIn",
            icon: "fa-linkedin",
            url: "https://www.linkedin.com/in/benjamin-zambelli/",
            color: "gray",
        },
        {
            name: "GitHub",
            icon: "fa-square-github",
            url: "https://github.com/BenJokek",
            color: "gray",
        },
        {
            name: "YouTube",
            icon: "fa-youtube",
            url: "https://www.youtube.com/channel/UCHAtb9BayfnlFDCGXKMiysA",
            color: "gray",
        },
    ];

    function handleMouseEnter(index) {
        socialLinks[index].color = "#00FFFF";
    }

    function handleMouseLeave(index) {
        socialLinks[index].color = "gray";
    }

    function handleFocus() {
        // Set color for "all1" link when focused
        socialLinks.forEach((link) => {
            if (link.name === "all1") {
                link.color = "#00CCCC";
            } else {
                link.color = "gray";
            }
        });
    }
</script>

<ul>
    {#each socialLinks as link, index}
        <li>
            <a
                href={link.url}
                target="_blank"
                on:mouseover={() => handleMouseEnter(index)}
                on:mouseleave={() => handleMouseLeave(index)}
                on:focus={handleFocus}
                style="color: {link.color}"
            >
                <i
                    class={"fa-brands " + link.icon + " fa-2xl"}
                    style="color: {link.color}"
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
        /* color: #808080; */
    }

    .fa-brands {
        padding: 25px;
    }
</style>
