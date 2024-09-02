async function fetchData(){
    const response = await fetch("https://www.codewithharry.com/tutorial/css-specificity/");
    console.log(" ~ fetchData ~ response", response)
    const data = await response.json();
    console.log("~ fetchData ~ data", data)
    console.log(" ~ data", data);
}

fetchData();