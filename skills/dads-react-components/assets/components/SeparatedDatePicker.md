# SeparatedDatePicker

元のフォルダ: `src/components/SeparatedDatePicker/`。`scripts/add_components.py` で個別のファイルに展開できる。

<!-- file: SeparatedDatePicker.tsx -->
````tsx
import type { ComponentProps } from 'react';

export type SeparatedDatePickerSize = 'lg' | 'md' | 'sm';

export type SeparatedDatePickerProps = Omit<ComponentProps<'div'>, 'children'> & {
  size?: SeparatedDatePickerSize;
  isError?: boolean;
  isReadonly?: boolean;
  isDisabled?: boolean;
  children: (props: {
    readOnly?: boolean;
    'aria-disabled'?: boolean;
    'aria-invalid'?: boolean;
  }) => JSX.Element;
};

export const SeparatedDatePicker = (props: SeparatedDatePickerProps) => {
  const { className, size = 'lg', isError, isReadonly, isDisabled, children, ...rest } = props;

  return (
    <div className='pt-3 inline-block'>
      <div
        className={`flex h-14 gap-x-4 text-solid-gray-900 data-[size=md]:h-12 data-[size=sm]:h-10 ${className ?? ''}`}
        data-size={size}
        {...rest}
      >
        {children({ readOnly: isReadonly, 'aria-disabled': isDisabled, 'aria-invalid': isError })}
      </div>
    </div>
  );
};
````

<!-- file: index.ts -->
````ts
export * from './parts/SeparatedDatePickerCalendarButton';
export * from './parts/SeparatedDatePickerDate';
export * from './parts/SeparatedDatePickerMonth';
export * from './parts/SeparatedDatePickerYear';
export * from './SeparatedDatePicker';
````

<!-- file: parts/SeparatedDatePickerCalendarButton.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';
import type { SeparatedDatePickerSize } from '../SeparatedDatePicker';

export type SeparatedDatePickerCalendarButtonProps = ComponentProps<'button'> & {
  size?: SeparatedDatePickerSize;
};

export const SeparatedDatePickerCalendarButton = forwardRef<
  HTMLButtonElement,
  SeparatedDatePickerCalendarButtonProps
>((props, ref) => {
  const { className, size = 'lg', ...rest } = props;

  return (
    <button
      className={`group flex h-14 items-center justify-center gap-x-1 rounded-6 border border-key-900 bg-white px-3 text-key-900 hover:border-[calc(3/16*1rem)] hover:px-2.5 focus-visible:outline focus-visible:outline-4 focus-visible:outline-offset-[calc(2/16*1rem)] focus-visible:outline-black focus-visible:ring-[calc(2/16*1rem)] focus-visible:ring-yellow-300 data-[size=md]:h-12 data-[size=sm]:h-10 ${className ?? ''}`}
      type='button'
      data-size={size}
      ref={ref}
      {...rest}
    >
      <svg width='24px' height='24px' viewBox='0 -960 960 960' role='img' aria-label='カレンダー'>
        <path
          d='M360-300q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29ZM200-80q-33 0-56.5-23.5T120-160v-560q0-33 23.5-56.5T200-800h40v-80h80v80h320v-80h80v80h40q33 0 56.5 23.5T840-720v560q0 33-23.5 56.5T760-80H200Zm0-80h560v-400H200v400Z'
          fill='currentcolor'
        />
      </svg>
      <svg className='size-4 group-aria-expanded:rotate-180' viewBox='0 0 24 24' aria-hidden={true}>
        <path d='M12 17.1L3 8L4 7L12 15L20 7L21 8L12 17.1Z' fill='currentcolor' />
      </svg>
    </button>
  );
});
````

<!-- file: parts/SeparatedDatePickerDate.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';

export type SeparatedDatePickerDateProps = Omit<ComponentProps<'input'>, 'placeholder'> & {
  placeholder?: never;
};

export const SeparatedDatePickerDate = forwardRef<HTMLInputElement, SeparatedDatePickerDateProps>(
  (props, ref) => {
    const { className, 'aria-disabled': disabled, readOnly, ...rest } = props;

    return (
      <label className='relative [&:has([aria-disabled="true"])]:pointer-events-none'>
        <span className='absolute inset-x-0 -top-3 mx-auto w-6 bg-white p-1 text-oln-16N-100 [&:has(+[aria-disabled=true])]:text-solid-gray-420 forced-colors:[&:has(+[aria-disabled=true])]:text-[GrayText]'>
          日
        </span>
        <input
          className={`h-full w-14 rounded-8 border border-solid-gray-600 bg-white text-center read-only:[&:not([aria-disabled="true"])]:border-dashed hover:border-solid-gray-900 hover:read-only:border-solid-gray-600 focus:border-solid-gray-900 focus:outline focus:outline-4 focus:outline-offset-[calc(2/16*1rem)] focus:outline-black focus:ring-[calc(2/16*1rem)] focus:ring-yellow-300 aria-disabled:bg-solid-gray-50 aria-disabled:text-solid-gray-420 aria-disabled:hover:border-solid-gray-600 aria-[invalid=true]:border-error-1 aria-[invalid=true]:hover:border-red-1000 forced-colors:[&:read-write]:aria-disabled:border-[GrayText] ${className ?? ''}`}
          type='text'
          inputMode='numeric'
          pattern='\d+'
          readOnly={disabled ? true : readOnly}
          aria-disabled={disabled}
          ref={ref}
          {...rest}
        />
      </label>
    );
  },
);
````

<!-- file: parts/SeparatedDatePickerMonth.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';

export type SeparatedDatePickerMonthProps = Omit<ComponentProps<'input'>, 'placeholder'> & {
  placeholder?: never;
};

export const SeparatedDatePickerMonth = forwardRef<HTMLInputElement, SeparatedDatePickerMonthProps>(
  (props, ref) => {
    const { className, 'aria-disabled': disabled, readOnly, ...rest } = props;

    return (
      <label className='relative [&:has([aria-disabled="true"])]:pointer-events-none'>
        <span className='absolute inset-x-0 -top-3 mx-auto w-6 bg-white p-1 text-oln-16N-100 [&:has(+[aria-disabled=true])]:text-solid-gray-420 forced-colors:[&:has(+[aria-disabled=true])]:text-[GrayText]'>
          月
        </span>
        <input
          className={`h-full w-14 rounded-8 border border-solid-gray-600 bg-white text-center read-only:[&:not([aria-disabled="true"])]:border-dashed hover:border-solid-gray-900 hover:read-only:border-solid-gray-600 focus:border-solid-gray-900 focus:outline focus:outline-4 focus:outline-offset-[calc(2/16*1rem)] focus:outline-black focus:ring-[calc(2/16*1rem)] focus:ring-yellow-300 aria-disabled:bg-solid-gray-50 aria-disabled:text-solid-gray-420 aria-disabled:hover:border-solid-gray-600 aria-[invalid=true]:border-error-1 aria-[invalid=true]:hover:border-red-1000 forced-colors:[&:read-write]:aria-disabled:border-[GrayText] ${className ?? ''}`}
          type='text'
          inputMode='numeric'
          pattern='\d+'
          readOnly={disabled ? true : readOnly}
          aria-disabled={disabled}
          ref={ref}
          {...rest}
        />
      </label>
    );
  },
);
````

<!-- file: parts/SeparatedDatePickerYear.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';

export type SeparatedDatePickerYearProps = Omit<ComponentProps<'input'>, 'placeholder'> & {
  placeholder?: never;
};

export const SeparatedDatePickerYear = forwardRef<HTMLInputElement, SeparatedDatePickerYearProps>(
  (props, ref) => {
    const { className, 'aria-disabled': disabled, readOnly, ...rest } = props;

    return (
      <label className='relative [&:has([aria-disabled="true"])]:pointer-events-none'>
        <span className='absolute inset-x-0 -top-3 mx-auto w-6 bg-white p-1 text-oln-16N-100 [&:has(+[aria-disabled=true])]:text-solid-gray-420 forced-colors:[&:has(+[aria-disabled=true])]:text-[GrayText]'>
          年
        </span>
        <input
          className={`h-full w-[calc(72/16*1rem)] rounded-8 border border-solid-gray-600 bg-white text-center read-only:[&:not([aria-disabled="true"])]:border-dashed hover:border-solid-gray-900 hover:read-only:border-solid-gray-600 focus:border-solid-gray-900 focus:outline focus:outline-4 focus:outline-offset-[calc(2/16*1rem)] focus:outline-black focus:ring-[calc(2/16*1rem)] focus:ring-yellow-300 aria-disabled:bg-solid-gray-50 aria-disabled:text-solid-gray-420 aria-disabled:hover:border-solid-gray-600 aria-[invalid=true]:border-error-1 aria-[invalid=true]:hover:border-red-1000 forced-colors:[&:read-write]:aria-disabled:border-[GrayText] ${className ?? ''}`}
          type='text'
          inputMode='numeric'
          pattern='\d+'
          readOnly={disabled ? true : readOnly}
          aria-disabled={disabled}
          ref={ref}
          {...rest}
        />
      </label>
    );
  },
);
````
