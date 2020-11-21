////////////////////////////////////////////////////////////////////////////////
//
//Problem 2: The Castle
//     1   2   3   4   5   6   7
//   #############################
// 1 #   |   #   |   #   |   |   #
//   #####---#####---#---#####---#
// 2 #   #   |   #   #   #   #   #
//   #---#####---#####---#####---#
// 3 #   |   |   #   #   #   #   #
//   #---#########---#####---#---#
// 4 # ->#   |   |   |   |   #   #
//   ############################# (Figure 1)
//
// #  = Wall
// |  = No wall
// -  = No wall
// -> = It points to the wall to remove according to the example output.
//
// Figure 1 shows the map of a castle. Write a program that calculates
// 1. how many rooms the castle has
// 2. how big the largest room is
// 3. which wall to remove from the castle to make as large a room as possible.
// The castle is divided into m * n (m<=50, n<=50) square modules.
// Each such module can have between zero and four walls.
//
// Input Data
// The map is stored in the INPUT.TXT file in the form of numbers,
// one for each module.
// + The file starts with the number of modules in the north-south direction
//   and the number of modules in the east-west direction.
// * In the following lines each module is described by a number (0<=p<=15).
//   This number is the sum of: 1 (= wall to the west), 2 (= wall to the north),
//   4 (= wall to the east), 8 (= wall to the south). Inner walls are defined twice;
//   a wall to the south in module 1,1 is also indicated as a wall to the north
//   in module 2,1.
// + The castle always has at least two rooms.
//
// INPUT.TXT for our example:
// 4
// 7
// 11  6 11  6  3 10  6
//  7  9  6 13  5 15  5
//  1 10 12  7 13  7  5
// 13 11 10  8 10 12 13
//
// Output Data
// In the OUTPUT.TXT file, the following are written on three lines:
// First the number of rooms, then the area of the largest room
// (counted in modules) and a suggestion of which wall to remove
// (first the row and then the column of the module next to the wall and
// finally the compass direction that points to the wall).
// In our example ("4 1 E" is one of several possibilities,
// you need only produce one): 5 9 4 1 E
//
const INPUT = `
4
7
11  6 11  6  3 10  6
 7  9  6 13  5 15  5
 1 10 12  7 13  7  5
13 11 10  8 10 12 13`;
/** Zom global stuff */
const WNES = [1, 2, 4, 8]; // West North East South
const DR = [{i:0, j:-1}, // W (dr = dx + dy)
            {i:-1, j:0}, // N
            {i:0, j:+1}, // E
            {i:+1, j:0}, // S
           ];
const BOOL = [(i, j, n, m) => (0 < j),       // What is this?
              (i, j, n, m) => (0 < i),       // N 
              (i, j, n, m) => (j < (m - 1)), // E Out of bounds cks.
              (i, j, n, m) => (i < (n - 1)), // S
             ];
const DIRECfN = {1: "West",
                 2: "North",
                 4: "East",
                 8: "South"};
/** Generate a matrix with n rows and m cols filled with fillValue */
function mtrx(n, m, fillValue) {
    if (n == 1) {
        return Array(m).fill(fillValue);
    } else {
        return Array(n).fill().map(() => Array(m).fill(fillValue));
    } // JavaScript is an AMAZING language!
}
class Castle {
    /** ibuf - input buffer (string) */
    constructor(ibuf) {
        /* Split to lines and discard empty entries. */
        ibuf = ibuf.split('\n').filter((l) => l.length);
        /* rows: 0 <= i < n */
        const n = Number(ibuf[0]);
        /* cols: 0 <= j < m */
        const m = Number(ibuf[1]);
        /* For the graph we are going to use the same input matrix */
        let g = new Array(n);
        for (let j = 0; j < n; ++j) {
            g[j] = ibuf[(2 + j)].split(' ').filter((l) => l.length);
            g[j] = g[j].map((n) => Number(n));
        }
        this.n = n;
        this.m = m;
        this.g = g;
    }
    /** W'r following the book of Dasgupta et al. here */
    explore(i, j) {
        this.room[i][j] = this.roomCntr; // previsit
        ++this.roomSiz[this.roomCntr];   // increment room size
        for (let d = 0; d < 4; ++d) {
            if (BOOL[d](i, j, this.n, this.m)) {
                let i1 = i + DR[d].i; // nbor's row
                let j1 = j + DR[d].j; // nbor's col
                /* Ck if there is a inner wall */
                if ((this.g[i][j] & WNES[d])) {
                    /* Ck if nbor room was visited */
                    let nbor = this.room[i1][j1];
                    /* Ck if visited but not in the same room. */
                    if ((-1 < nbor) && (nbor != this.roomCntr)) {
                        /* register a backdoor (hidden wolf3d typeof door) */
                        this.internet[nbor][this.roomCntr] = [i, j, WNES[d]];
                        this.internet[this.roomCntr][nbor] = [i, j, WNES[d]];
                    }
                } else { /* explore */
                    if (this.room[i1][j1] == -1) {
                        this.explore(i1, j1);
                    } //--------------------------------------------------------
                } //------------------------------------------------------------
            } //--------------- Luke,.. look, ko7ko MHoro 7yk! -----------------
        } //--------------------------------------------------------------------
    } //------------------------------------------------------------------------
////////////////////////////////////////////////////////////////////////////////    
    /** Depth First Search */
    dfs() {
        const n = this.n;
        const m = this.m;
        /* maximum number of rooms */
        this.maxRooms = (n*m);
        /* modules' connectivity counter, also used for is visited ck */
        this.room = mtrx(n, m, -1);
        this.roomCntr = 0; // room counter
        /* No= modules per room */
        this.roomSiz = mtrx(1, this.maxRooms, 0);
        /* Inner walls room conections */
        this.internet = mtrx(this.maxRooms, this.maxRooms, undefined);
        for (let i = 0; i < n; ++i) {
            for (let j = 0; j < m; ++j) {
                if (this.room[i][j] == -1) { // not visited
                    this.explore(i, j);
                    ++this.roomCntr;
                }
            }
        } /* c7aBu r7ynaKa */
    }
    /** Find maximum inter connection. */
    ping() {
        let n = this.roomCntr;
        let inet = this.internet;
        let siz = this.roomSiz;
        let mxsiz2 = 0; // Maximum combined size of 2 rooms
        let StereoMCs;  // connected
        for (let i = 0; i < n; ++i) {
            for (let j = i + 1; j < n; ++j) {
                if (inet[i][j] != undefined) {
                    let siz2 = siz[i] + siz[j];
                    if (mxsiz2 < siz2) {
                        mxsiz2 = siz2;
                        StereoMCs = inet[i][j];
                    }
                }
            }
        }
        let [i, j, k] = StereoMCs;
        console.log("[" + i + "," + j + "]: " + DIRECfN[k]);
    }
}
let castle = new Castle(INPUT);
castle.dfs();
console.log(castle.room);
castle.ping();

////////////////////////////////////////////////////////////////////////////////
// log:
// > For running the program open TheCastle.html with a browser and open the
//   deelopment console (Chrome:F12), reloding the page will restart the script.
// > Ktge cTe TptrHa7u? HsMaTe HuTo eBpo, HuTo Bu3us!
