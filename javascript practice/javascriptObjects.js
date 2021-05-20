var worker1 = {Name: "Betty", yearsOfExperience: 12, Gender: "F", Age: 32,}

function worker (name, yearsOfExperience, gender, age){
    this.name=name;
    this.yearsOfExperience=yearsOfExperience;
    this.gender=gender;
    this.age=age;
}

// Adding individual information through code.
function Worker (name, yearsOfExperience, gender, age){
    this.name=name;
    this.yearsOfExperience=yearsOfExperience;
    this.gender=gender;
    this.age=age;
}
var worker2=new Worker("Timmy", 2, "M", 26);