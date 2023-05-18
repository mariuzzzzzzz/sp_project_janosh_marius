<script>
    var globalVariable = "empty";

    let selectedOption = {
        option1: "",
        option2: "",
    };

    function updateSelectedOption1(event) {
        selectedOption.option1 = event.target.value;
        console.log(selectedOption);
    }

    function updateSelectedOption2(event) {
        selectedOption.option2 = event.target.value;
        console.log(selectedOption);
    }

    function handleCommit() {
        let x = 0;
        let y = 0;

        if (selectedOption.option1 === "overtime") {
            x = 1;
        } else if (selectedOption.option1 === "GLAZ") {
            x = 2;
        } else if (selectedOption.option1 === "COVID-Hours") {
            x = 3;
        } else if (selectedOption.option1 === "IST") {
            x = 4;
        } else if (selectedOption.option1 === "SOLL") {
            x = 5;
        } else if (selectedOption.option1 === "sollist") {
            x = 6;
        } else if (selectedOption.option1 === "Ferien") {
            x = 7;
        }

        if (selectedOption.option2 === "cases") {
            y = 1;
        } else if (selectedOption.option2 === "hospitalisation") {
            y = 2;
        }

        console.log("x:", x, "y:", y);
        globalVariable = x.toString() + y.toString();
        console.log(globalVariable);
    }
</script>

<h1>Comparison Page</h1>
<h3>!SELECT YOU VALUES!</h3>
<select id="employeeData" on:change={updateSelectedOption1}>
    <option value="">data employee</option>
    <option value="overtime">overtime</option>
    <option value="GLAZ">GLAZ</option>
    <option value="COVID-Hours">Explicit COVID Workhours</option>
    <option value="IST">IST</option>
    <option value="SOLL">Soll</option>
    <option value="sollist">soll-ist</option>
    <option value="Ferien">Holidays</option>
</select>

<select id="covidData" on:change={updateSelectedOption2}>
    <option value="">data covid</option>
    <option value="cases">cases</option>
    <option value="hospitalisation">hospitalisation</option>
</select>

<button on:click={handleCommit} disabled={selectedOption.option1 == 0|| selectedOption.option2 == 0}>
    show graph
</button>


<div />

<img src="/img/plot{globalVariable}.png" alt="plot" />

<style>
    h1 {
        padding-top: 50px;
        padding-bottom: 20px;
    }
    div {
        padding-top: 30px;
    }
</style>
