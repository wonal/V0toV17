
async function testFunction(){
    const response = await fetch('http://localhost:8000/V0toV17/1/entries/');
    const data = await response.json();
    const list = document.getElementById("entries");
    for (const str of data){
        const item = document.createElement("li");
        item.innerText = str;
        list.appendChild(item);
    }
}

testFunction();