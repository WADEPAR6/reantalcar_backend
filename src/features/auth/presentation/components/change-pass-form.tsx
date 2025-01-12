/* eslint-disable react-hooks/rules-of-hooks */
'use client';

import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import { IRecoveryPassword } from '../../models/IRecovery';
import { useChangePassword } from '../../hooks/useChangePassword';
import { useSearchParams } from 'next/navigation';

export const ChangePassForm = () => {
  const { initialValues, validationSchema, onSubmit } = useChangePassword();
  const searchParams = useSearchParams();
  const reset_password_token = searchParams.get('reset_password_token');

  if (!reset_password_token) {
    return <div>Error: No se encontró el token de recuperación</div>;
  }

  const {
    register,
    formState: { errors },
    handleSubmit,
  } = useForm<Omit<IRecoveryPassword, 'reset_password_token'>>({
    resolver: yupResolver(validationSchema),
    defaultValues: initialValues,
  });

  return (
    <form
      onSubmit={handleSubmit((data) => onSubmit(data, reset_password_token))}
      className="flex flex-col w-full max-w-sm p-6 bg-white shadow-md border border-gray-200 rounded-2xl"
    >
      <label htmlFor="password" className="text-base font-medium pb-3">
        Contraseña
      </label>
      <input
        id="password"
        type="password"
        {...register('password')}
        placeholder="Contraseña"
        className="mb-3 p-2 border rounded-lg focus:outline-none focus:ring-1 focus:ring-gray-400"
      />
      <span className="text-red-500 text-sm">{errors.password?.message}</span>

      <label htmlFor="password_confirmation" className="text-base font-medium pb-3">
        Confirmar contraseña
      </label>
      <input
        id="password_confirmation"
        type="password"
        {...register('password_confirmation')}
        placeholder="Confirmar contraseña"
        className="mb-3 p-2 border rounded-lg focus:outline-none focus:ring-1 focus:ring-gray-400"
      />
      <span className="text-red-500 text-sm">{errors.password_confirmation?.message}</span>
      <button
        type="submit"
        className="transition-colors mt-4 bg-new-black text-white p-2 rounded-lg hover:bg-new-back-hover"
      >
        Enviar
      </button>
    </form>
  );
};
