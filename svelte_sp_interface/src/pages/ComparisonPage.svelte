<script>
    var globalVariable = "00";
    var teamLink = "";

    let selectedOption = {
        option1: 0,
        option2: 0,
        option3: "",
    };

    function updateSelectedOption1(event) {
        selectedOption.option1 = event.target.value;
        console.log(selectedOption);
    }

    function updateSelectedOption2(event) {
        selectedOption.option2 = event.target.value;
        console.log(selectedOption);
    }
    function updateSelectedOption3(event) {
        selectedOption.option3 = event.target.value;
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
        } else if (selectedOption.option2 === "ICU") {
            y = 3;
        } else if (selectedOption.option2 === "deaths") {
            y = 4;
        }

        if(selectedOption.option3 ==="DST IPS"){
            teamLink = "DST IPS"
        }else if(
            selectedOption.option3 ==="DST NF"
        ){
            teamLink = "DST NF"
        }
        else if(
            selectedOption.option3 ==="DST OPS"
        ){
            teamLink = "DST OPS"
        }
        console.log("x:", x, "y:", y);
        globalVariable = x.toString() + y.toString();
        console.log(globalVariable);
    }

</script>



<h1>Comparison Page</h1>
<h3>!SELECT YOUR VALUES!</h3>
<div class="dropdown-container">
  <div class="dropdown-wrapper">
    <h5>Employee Data</h5>
    <select id="employeeData" on:change={updateSelectedOption1} class="dropdown">
        <option value="">data employee</option>
    <option value="overtime">overtime</option>
    <option value="GLAZ">GLAZ</option>
    <option value="COVID-Hours">Explicit COVID Workhours</option>
    <option value="IST">IST</option>
    <option value="SOLL">Soll</option>
    <option value="sollist">soll-ist</option>
    <option value="Ferien">Holidays</option>
    </select>
  </div>
  <div class="dropdown-wrapper">
    <h5>Covid Data</h5>
    <select id="covidData" on:change={updateSelectedOption2} class="dropdown">
        <option value="">data covid</option>
    <option value="cases">cases</option>
    <option value="hospitalisation">hospitalisation</option>
    <option value="ICU">ICU_Cases</option>
    <option value="deaths">Deaths</option>
    </select>
  </div>
  <div class="dropdown-wrapper">
    <h5>Team Selection</h5>
    <select id="Team" on:change={updateSelectedOption3} class="dropdown">
        <option value="">Select Team</option>
        <option value="DST IPS">ICU-Team</option>
        <option value="DST NF">Emergency-Team</option>
        <option value="DST OPS">Operation-Team</option>
    </select>
  </div>
</div>

<div class = "button-container">
    <button
    on:click={handleCommit}
    disabled={selectedOption.option1 == 0 || selectedOption.option2 == 0 || selectedOption.option3 == "" }
    class = "button">
    show graph
</button>
</div>

<div class="image-container">
    <img src="/img/{teamLink}/plot{globalVariable}.png" alt="plot" class="centered-image" />
  </div>
  

<style>
    h1 {
        padding-top: 20px;
        padding-bottom: 20px;
        text-align: center;
    }
    h3 {
        text-align: center;
    }
    div {
        padding-top: 30px;
    }

</style>
