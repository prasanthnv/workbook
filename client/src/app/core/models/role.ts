export interface Role {
  id?: number;
  name: string;
  createdAt?: Date;
  updatedAt?: Date;
}

export enum RoleTypes {
  ADMIN = 'ADMIN',
  MANAGER = 'MANAGER',
  USER = 'USER',
}
