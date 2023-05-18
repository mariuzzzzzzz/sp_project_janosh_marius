<script>
	import Router from "svelte-spa-router"
	import routes from "./routes"
</script>

<div id="app">
	<nav>
		<a href="#/">Home</a>
		<a href="#/DataPage">Data</a>
		<a href="#/ComparisonPage">Comparison</a>
	</nav>

	<Router {routes}/>
</div>