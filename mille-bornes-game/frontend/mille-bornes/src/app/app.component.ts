import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
 selector: 'app-root',
 templateUrl: './app.component.html',
 styleUrls: ['./app.component.css']
})
export class AppComponent {
 gameState: any;

 constructor(private http: HttpClient) {}

 startGame() {
   this.http.post('http://localhost:5000/start_game', {}).subscribe(data => {
     this.gameState = data;
   });
 }

 playCard(card: any) {
   this.http.post('http://localhost:5000/play_card', { card: card }).subscribe(data => {
     this.gameState = data;
   });
 }
}