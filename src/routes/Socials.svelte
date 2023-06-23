<script>
    let socialLinks = [
        {
            name: "LinkedIn",
            icon: "fa-brands fa-linkedin",
            url: "https://www.linkedin.com/in/benjamin-zambelli/",
            color: "gray",
        },
        {
            name: "GitHub",
            icon: "fa-brands fa-square-github",
            url: "https://github.com/BenJokek",
            color: "gray",
        },
        {
            name: "YouTube",
            icon: "fa-brands fa-youtube",
            url: "https://www.youtube.com/channel/UCHAtb9BayfnlFDCGXKMiysA",
            color: "gray",
        },
        {
            name: "Resume",
            icon: "fa-solid fa-file",
            url: "https://drive.google.com/file/d/1F41PiKibBZF_gyktlLQ7Z03EQ6hNP_2p/view?usp=sharing",
            color: "gray",
        }
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
                    class="{link.icon} fa-2xl"
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
        display: flex;
    }
    li {
        text-align: center;
    }

    .socials {
        padding: 5px;
    }

    .fa-2xl {
        padding: 25px;
    }

    @media (min-width: 800px) {
		.fa-2xl {
        padding: 40px;
    }
	}
</style>
