
export interface IUser {
    id: number | undefined;
    role: string;
    email:     string;
    password:  string;
    name:      string;
    lastname:  string;
    address:   string;
    phone:     string;
    birthdate: Date;
    username:  string;
}


export interface IUserResponse {
    code:    number;
    message: string;
    data:    IUser;
}

