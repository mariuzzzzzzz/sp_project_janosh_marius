<script>
	import Router from "svelte-spa-router"
	import routes from "./routes"
</script>

<div id="app">
	<nav>
		<a href="#/">Home</a>

		<!-- TODO: add a link to "#/products" -->
		<a href="#/DataPage">Data</a>
		
		<a href="#/ComparisonPage">Comparison</a>
	</nav>

	<Router {routes}/>
</div>