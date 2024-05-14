the_heading = document.getElementById("title");

the_name = document.getElementById("characterName");

the_description = document.getElementById("characterDescription");

function changeName() {
	name_entry = document.getElementById("characterNameEntry");
	var name = name_entry.value;
	var text = "Name: " + name + "<br> ";
	the_name.innerHTML = "" + text;
}

function changeStats() {
	the_heading.innerHTML = "Make Another Character?";
		
	var raceArray = ["Human", "Goblin", "Dwarf", "Elf", "Gnome", "Hafling"];
	var race = raceArray[Math.floor(Math.random() * 6)];
	var text = "Race: " + race + "<br>";
  
	var age = randomStatNumber(200);
	text = text + "Age: " + age + "<br>";
	var strength = randomStatNumber(12);
	text = text + "Strength Level: " + strength + "<br>";
	var constitution = randomStatNumber(12);
	text = text + "Constitution Level: " + constitution + "<br>";
	var dexterity = randomStatNumber(12);
	text = text + "Dexterity Level: " + dexterity + "<br>";
	var intelligence = randomStatNumber(12);
	text = text + "Intelligence Level: " + intelligence + "<br>";
	var wisdom = randomStatNumber(12);
	text = text + "Wisdom Level: " + wisdom + "<br>";
	var charisma = randomStatNumber(12);
	text = text + "Charisma Level: " + charisma + "<br>";
  
  the_description.innerHTML = text;
}

function randomStatNumber(max) {
	return (Math.floor(Math.random() * max)) + 5;
}

