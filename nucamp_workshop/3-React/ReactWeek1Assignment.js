class Student {
  constructor(name, email, community) {
    this.name = name;
    this.email = email;
    this.community = community;
  }
}

class Bootcamp {
  constructor(name, level, student = []) {
    this.name = name;
    this.level = level;
    this.student = student;
  }

  registerStudent(studentToRegister) {
    if (
      this.student.filter((a) => a.email == studentToRegister.email).length ===
      0
    ) {
      this.student.push(studentToRegister);
      console.log(`Your email(${studentToRegister.email}) is successfully registered.`);
    } else {
      console.log("This email has been already registered.");
    }
    return this.student;
  }
}

const Nathan = new Student("Nathan", "nathan@na.com", "Washington");
const Edwin = new Student("Edwin", "nathan@na.com", "Washington");
const bootstrap = new Bootcamp("bootstrap", 1);
