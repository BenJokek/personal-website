<script>
    import { page } from "$app/stores";
    import round_text from "../lib/images/round-text.png";
</script>

<div class="container">
    <a
        href="/projects"
        class="go-to-project-btn"
        data-animation="rotate_up"
        class:selected={$page.url.pathname.startsWith("/projects")}
    >
        <img src={round_text} alt="Rounded text" />
        <i class="fa-sharp fa-regular fa-star fa-2xl" />
    </a>
</div>

<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0;
    }

    .go-to-project-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        width: 200px;
        height: 200px;
    }

    .go-to-project-btn img {
        width: 80%;
        height: 80%;
        animation: rotate 5s linear infinite;
    }

    @keyframes rotate {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }

    .go-to-project-btn i {
        position: absolute;
        opacity: 1;
    }
</style>
