<script>
	// Track the active page
	export let activePage = "";

	// Handle navigation clicks
	function navigate(page) {
		activePage = page;
	}
</script>

<nav>
	<ul>
	  <li>
		<a href="#" class:selected={activePage === 'data'} on:click={() => navigate('data')}>
		  Data
		</a>
	  </li>
	  <li>
		<a href="#" class:selected={activePage === 'comparison'} on:click={() => navigate('comparison')}>
		  Comparison
		</a>
	  </li>
	</ul>
  </nav>
  
<style>
	nav {
    background-color: #f1f1f1;
    padding: 10px;
  }

  ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: flex;
  }

  li {
    margin-right: 10px;
  }

  a {
    text-decoration: none;
    color: #333;
    padding: 5px;
    border-radius: 3px;
  }

  a.selected {
    background-color: #333;
    color: #fff;
  }
</style>
