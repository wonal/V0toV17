const URL = '/V0toV17';

class ClimbingEntries{
    constructor() {
        this.entries = [];
    }

    async retrieveEntries() {
        const response = await fetch(`${URL}/1/entries/`);
        const data = await response.json();
        const climbs = [];
        const parsedData = JSON.parse(data);
        for(const dto of parsedData){
            climbs.push(this.formatEntries(dto));
        }
        return climbs;
    }

    formatEntries(objData){
        const climbs = [];
        climbs.push(formatDate(objData.fields.session[0]));
        climbs.push(`V${objData.fields.v_grade}`);
        climbs.push(`${objData.fields.num_success}`); 
        climbs.push(`${objData.fields.num_attempts}`); 
        climbs.push(`${objData.fields.session[1]}`); 
        return climbs;
    }

    async render(){
        this.entries = await this.retrieveEntries();
        const table = document.getElementById("entries");
        for (const entry of this.entries) {
            const row = document.createElement("tr");
            for (const data of entry){
                const col = document.createElement("td");
                col.innerText = data;
                row.appendChild(col);
            }
            table.appendChild(row);
        }
    }
}

/* Assumes input format of: 2019-06-10T17:48:30.243Z
   and return format is: 06/10/2019 - 17:48 */
function formatDate(date){
    let result = "";
    const dateTime = date.split('T');
    const datePortion = dateTime[0].split('-');
    result += `${datePortion[1]}/${datePortion[2]}/${datePortion[0]} - `;
    const timePortion = dateTime[1].split('.')[0].split(':');
    result += `${timePortion[0]}:${timePortion[1]}`;
    return result;
}

const climbLog = new ClimbingEntries();
climbLog.render();