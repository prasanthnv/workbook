import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { WorkbookRoutingModule } from './workbook-routing.module';
import { DashboardComponent } from './pages/dashboard/dashboard.component';

@NgModule({
  declarations: [DashboardComponent],
  imports: [CommonModule, WorkbookRoutingModule],
})
export class WorkbookModule {}
