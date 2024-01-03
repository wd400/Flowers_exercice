import { Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { AddComponent } from './add/add.component';
import { TrainComponent } from './train/train.component';
import { PredictComponent } from './predict/predict.component';
import { TestLossComponent } from './test-loss/test-loss.component';
import { ListComponent } from './list/list.component';



export const routes: Routes = [
  { path: 'add', component: AddComponent },
  { path: 'list', component: ListComponent },
  { path: 'train', component: TrainComponent },
  { path: 'predict', component: PredictComponent },
  { path: 'test_loss', component: TestLossComponent },

];