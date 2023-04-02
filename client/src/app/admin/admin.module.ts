import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AdminRoutingModule } from './admin-routing.module';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { UsersComponent } from './pages/users/users.component';
import { ButtonModule } from 'primeng/button';
@NgModule({
  declarations: [DashboardComponent, UsersComponent],
  imports: [CommonModule, AdminRoutingModule, ButtonModule],
})
export class AdminModule {}
