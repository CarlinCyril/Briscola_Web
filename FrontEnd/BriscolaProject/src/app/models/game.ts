import { Player } from './player';

export class Game {

    public uuid: string
    public name: string;
    public gameType: string;
    public numMaxPlayers: number;
    public players: Array<Player>;

    constructor(name: string, gameType: string, numMaxPlayers: number) {
        this.name = name;
        this.gameType = gameType;
        this.numMaxPlayers = numMaxPlayers;
        this.players = new Array<Player>()
    }
}