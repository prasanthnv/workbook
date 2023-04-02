import { Role } from './role';

export interface User {
  id?: number;
  name: string;
  email: string;
  password?: string;
  role: Role;
  createdAt?: Date;
  updatedAt?: Date;
}
