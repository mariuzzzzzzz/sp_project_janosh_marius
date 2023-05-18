<script>
    let selectedOption1 = "";
    let selectedOption2 = "";

    // Handle the change event when an option is selected
    function handleChange1(event) {
        selectedOption1 = event.target.value;
    }
    function handleChange2(event) {
        selectedOption2 = event.target.value;
    }
    function handleCommit() {
        let x = 0;
        let y = 0;

        if (selectedOption1 == "overtime" && selectedOption2 == "cases") {
            let x = 1;
            let y = 1;
        } else if (
            selectedOption1 == "overtime" &&
            selectedOption2 == "hospitalisation"
        ) {
            let x = 1;
            let y = 2;
        } else if (selectedOption1 == "sollist" && selectedOption2 == "cases") {
            let x = 6;
            let y = 1;
        } else {
            let x = 6;
            let y = 2;
        }
    }
</script>

<h1>Comparison Page</h1>

<select bind:value={selectedOption1} on:change={handleChange1}>
    <option value="">data employee</option>
    <option value="overtime">overtime</option>
    <option value="sollist">soll-ist</option>
</select>

<select bind:value={selectedOption2} on:change={handleChange2}>
    <option value="">data covid</option>
    <option value="cases">cases</option>
    <option value="hospitalisation">hospitalisation</option>
</select>

<button on:click={handleCommit}>Commit</button>

<style>
    h1 {
        padding-top: 50px;
        padding-bottom: 20px;
    }
</style>
