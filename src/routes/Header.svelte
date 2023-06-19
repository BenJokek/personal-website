<script>
	import { Hamburger } from "svelte-hamburgers";
	import Menu from "./Menu.svelte";
	let open;
</script>

<header>
	<Hamburger bind:open --color="white" type="emphatic" />

	<Menu bind:open />
</header>

<style>
</style>
