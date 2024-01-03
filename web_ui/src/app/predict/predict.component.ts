import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormGroup, FormControl, Validators, ReactiveFormsModule } from '@angular/forms';
import { environment } from '../../environments/environment';


@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.sass'],
  standalone: true,
  imports: [ ReactiveFormsModule],
})
export class PredictComponent {
  predictForm= new FormGroup({
    x: new FormControl(3, Validators.required)
  });

  constructor(private http: HttpClient) {

  }

  predict() {
    if (this.predictForm.valid) {
      this.http.post('/api/predict',
        {
          x: this.predictForm.value.x
        }
      ).subscribe(response => {
        alert(JSON.stringify(response));
      });
    }
  }
}