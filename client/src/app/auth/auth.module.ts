import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AuthRoutingModule } from './auth-routing.module';
import { LoginComponent } from './pages/login/login.component';
import { ResetpasswordComponent } from './pages/resetpassword/resetpassword.component';

@NgModule({
  declarations: [LoginComponent, ResetpasswordComponent],
  imports: [CommonModule, AuthRoutingModule],
})
export class AuthModule {}
