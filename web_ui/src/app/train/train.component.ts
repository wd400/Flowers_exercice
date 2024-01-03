import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-train',
  standalone: true,
  imports: [],
  templateUrl: './train.component.html',
  styleUrl: './train.component.sass'
})

export class TrainComponent {
  constructor(private http: HttpClient) { }

  trainModel() {
    this.http.get('/api/train').subscribe(response => {
      alert(JSON.stringify(response));
    });
  }
}