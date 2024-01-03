import { AfterViewInit, Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-test-loss',
  templateUrl: './test-loss.component.html',
  styleUrl: './test-loss.component.sass',
  standalone: true,
  providers: [HttpClient,CommonModule],
  imports: [CommonModule]


})
export class TestLossComponent {
loadLoss() {

      this.http.get<{ loss: number, error: string }>('/api/test_loss').subscribe(response => {
      this.loss = response.loss;
      this.error = response.error;
    });


}
  loss: number | undefined;
  error: string | undefined;

  constructor(private http: HttpClient) { }



  ngOnInit() {
    //execute only if on client side
    if (typeof window === 'undefined') {
      return;
    }
   this.loadLoss();
  }




  

}