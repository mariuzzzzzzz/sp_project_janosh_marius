<script>
	import Router from "svelte-spa-router";
	import routes from "./routes";

	import "bootstrap/dist/css/bootstrap.min.css";
	import "bootstrap/dist/js/bootstrap.bundle.min.js";
</script>

<div id="app">
	<nav
		class="navbar navbar-expand-lg bg-body-tertiary justify-content-center"
	>
		<div class="container-fluid d-flex flex-column align-items-center">
			<a class="navbar-brand mb-3" href="/">COVIDxEMPLOYEES</a>
			<div
				class="collapse navbar-collapse justify-content-center"
				id="navbarNav"
			>
				<ul class="navbar-nav">
					<li class="nav-item">
						<button
							class="btn btn-sm btn-outline-primary"
							type="button"
							onclick="location.href='#/'">Home</button
						>
					</li>
					<li class="nav-item">
						<button
							class="btn btn-sm btn-outline-primary"
							type="button"
							onclick="location.href='#/ComparisonPage'"
							>Comparison</button
						>
					</li>
				</ul>
			</div>
		</div>
	</nav>

	<Router {routes} />
</div>

<style>
	.navbar-nav .nav-item {
		margin-right: 10px;
		margin-left: 10px;
	}
	.navbar-brand {
		display: inline-block;
		background-color: black;
		color: white;
		padding: 5px 10px;
	}
	:global(body) {
		background-color: rgba(68, 149, 255, 0.239);
	}
</style>
