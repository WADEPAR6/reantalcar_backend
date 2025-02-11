import * as yup from "yup";
import { IUser, IUserCreate } from "../models/IUser";
import { lastDayOfDecade } from "date-fns";
import { useUserStore } from "../context/user-store";
import { useRouter } from "next/navigation";

export const useUserForm = (currentUser?: Partial<IUser>) => {
  const {createUser, updateUser} = useUserStore();
  const router = useRouter();
  const initialValues: Partial<IUser> = {
    email: currentUser?.email || "",
    password: currentUser?.password || "",
    name: currentUser?.name || "",
    lastname: currentUser?.lastname || "",
    address: currentUser?.address || "",
    role: currentUser?.role || "",
    phone: currentUser?.phone || "",
birthdate: currentUser?.birthdate ? new Date(currentUser.birthdate) : new Date(),
    username: currentUser?.username || "",
  };

  const validationSchema = yup.object().shape({
    email: yup.string().email("El email no es válido").required("El email es requerido"),
    password: yup.string().required("La contraseña es requerida"),
    name: yup.string().required("El nombre es requerido").matches(/^[a-zA-Z]{3,}$/, "El nombre no es válido"),
    lastname: yup.string().required("El apellido es requerido").matches(/^[a-zA-Z]{3,}$/, "El apellido no es válido"),
    address: yup.string().required("La dirección es requerida").matches(/^[a-zA-Z0-9\s,.'-]{3,}$/, "La dirección no es válida"),
    role: yup.string().required("El rol es requerido"),
    phone: yup.string().required("El teléfono es requerido").matches(/^[0-9]+$/, "El teléfono solo puede contener números").min(10).max(10),
    birthdate: yup.date().required("La fecha de nacimiento es requerida").max(lastDayOfDecade(new Date())),
    username: yup.string().required("El nombre de usuario es requerido"),
  })

  const onSubmit = (values: IUserCreate) => {
    // eslint-disable-next-line @typescript-eslint/no-unused-expressions
    currentUser ? updateUser(currentUser.id as number, values): createUser(values)
    router.push('/dashboard/users/view')
  }

  return {
    initialValues,
    validationSchema,
    onSubmit
  }
};
