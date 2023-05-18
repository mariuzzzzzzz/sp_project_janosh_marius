<script>
	import Router from "svelte-spa-router";
	import routes from "./routes";

	import "bootstrap/dist/css/bootstrap.min.css";
	import "bootstrap/dist/js/bootstrap.bundle.min.js";
</script>

<div id="app">
	<nav class="navbar navbar-expand-lg bg-body-tertiary">
		<div class="container-fluid">
			<span class="navbar-brand" href="/">COVIDxEMPLOYEES</span>
			<button
				class="navbar-toggler"
				type="button"
				data-bs-toggle="collapse"
				data-bs-target="#navbarNav"
				aria-controls="navbarNav"
				aria-expanded="false"
				aria-label="Toggle navigation"
			>
				<span class="navbar-toggler-icon" />
			</button>
			<div class="collapse navbar-collapse" id="navbarNav">
				<ul class="navbar-nav">
					<li class="nav-item">
						<button
							class="btn btn-success"
							type="button"
							onclick="location.href='#/'">Home</button
						>
					</li>
					<li class="nav-item">
						<button
							class="btn btn-danger"
							type="button"
							onclick="location.href='#/DataPage'">Data</button
						>
					</li>
					<li class="nav-item">
						<button
							class="btn btn-warning"
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
	}
	.navbar-brand {
    display: inline-block;
    background-color: black;
    color: white;
    padding: 5px 10px;
    border-radius: 70%;
    position: relative;
  }
</style>
