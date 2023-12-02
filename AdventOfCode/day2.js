const fs = require("fs");
const txtFilePath = "../data/day2.txt";

// type round = {
//   redCount: number,
//   greenCount: number,
//   blueCount: number,
// }
// type game = {
//   id: number,
//   rounds: round[],
// }

const redLimit = 12;
const greenLimit = 13;
const blueLimit = 14;

const sumValidGameIds = (text) => {
  const gameStringArray = text.split("\n");
  // turn gameStringArray items into a game[]
  const games = gameStringArray.map((gameString, index) => {
    // init newGame object with id
    const newGame = { id: index + 1 };
    // remove 'Game #: ' from each line & split into individual round on '; '
    const roundsString = gameString.split(": ")[1].split("; ");
    const rounds = roundsString.map((roundStr) => {
      const newRound = roundStr.split(", ").map((r) => r.split(" "));

      //init formattedRound object may need to change intiial vals to null???
      const formattedRound = {
        redCount: 0,
        greenCount: 0,
        blueCount: 0,
      };
      newRound.forEach((colorQuantity) => {
        // check index [1] for color
        if (colorQuantity[1] === "red") {
          // overwrite colorCount to parseInt(colorQuantity[0])
          formattedRound.redCount = parseInt(colorQuantity[0]);
        }
        if (colorQuantity[1] === "green") {
          // overwrite colorCount to parseInt(colorQuantity[0])
          formattedRound.greenCount = parseInt(colorQuantity[0]);
        }
        if (colorQuantity[1] === "blue") {
          // overwrite colorCount to parseInt(colorQuantity[0])
          formattedRound.blueCount = parseInt(colorQuantity[0]);
        }
      });

      console.log("round: ", formattedRound);
      return formattedRound;
    });

    newGame["rounds"] = rounds;
    return newGame;
  });
  console.log("games: ", games);

  let validGamesIdSum = 0;
  // iterate over games
  games.forEach((game) => {
    //init isValidGame boolean
    let isValidGame = true;
    // forEach game iterate over rounds
    game.rounds.forEach((round) => {
      // if round.colorCount > corresponding colorLimit
      if (round.redCount > redLimit) {
        // update isValidGame to false and break
        isValidGame = false;
      }
      if (round.greenCount > greenLimit) {
        // update isValidGame to false and break
        isValidGame = false;
      }
      if (round.blueCount > blueLimit) {
        // update isValidGame to false and break
        isValidGame = false;
      }
    });
    // if game is valid, add game.id to validGamesIdSum
    if (isValidGame) {
      validGamesIdSum += game.id;
    }
  });

  return validGamesIdSum;
};

const example = `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`;
console.log("example sum: ", sumValidGameIds(example));

fs.readFile(txtFilePath, "utf8", (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  // console.log("input sum: ", sumValidGameIds(data));
});
