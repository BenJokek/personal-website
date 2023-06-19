<script>
    import { page } from "$app/stores";
    import { scale } from "svelte/transition";
    import { quadOut } from "svelte/easing";

    export let open;
</script>

{#if open}
    <nav>
        <ul>
            <li aria-current={$page.url.pathname === "/" ? "page" : undefined}>
                <a href="/" class:selected={$page.url.pathname === "/"}>Home</a>
            </li>
            <li
                aria-current={$page.url.pathname === "/works"
                    ? "page"
                    : undefined}
            >
                <a
                    href="/projects"
                    class:selected={$page.url.pathname === "/projects"}>Projects</a
                >
            </li>
            <li
                aria-current={$page.url.pathname.startsWith("/contact")
                    ? "page"
                    : undefined}
            >
                <a
                    href="/contact"
                    class:selected={$page.url.pathname.startsWith("/contact")}
                    >Contact</a
                >
            </li>
        </ul>
    </nav>

    <hr transition:scale={{ duration: 300, easing: quadOut, opacity: 1 }} />
{/if}

<style>
    @import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

    nav {
        text-align: center;
        font-size: 1.5em;
        letter-spacing: 0.15em;
        padding: 1em;
        padding-top: 0;
        color: #eef;
        font-family: 'Bangers', cursive;
        font-size: 1.5rem;
    }

    ul {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        justify-content: center;
    }

    li {
        margin: 0 1em;
    }

    a {
        text-decoration: none;
        color: gray;
    }

    a.selected {
        color: white;
    }

    a:hover {
        text-decoration: none;
    }
</style>
