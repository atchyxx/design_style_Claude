# DatePicker

元のフォルダ: `src/components/DatePicker/`。`scripts/add_components.py` で個別のファイルに展開できる。

<!-- file: DatePicker.tsx -->
````tsx
'use client';

import { type ComponentProps, type KeyboardEvent, type Ref, useRef } from 'react';

export type DatePickerSize = 'lg' | 'md' | 'sm';

export type DatePickerProps = Omit<ComponentProps<'div'>, 'children'> & {
  size?: DatePickerSize;
  isError?: boolean;
  isReadonly?: boolean;
  isDisabled?: boolean;
  children: (props: {
    yearRef: Ref<HTMLInputElement>;
    monthRef: Ref<HTMLInputElement>;
    dateRef: Ref<HTMLInputElement>;
    readOnly?: boolean;
    'aria-disabled'?: boolean;
    'aria-invalid'?: boolean;
  }) => JSX.Element;
};

export const DatePicker = (props: DatePickerProps) => {
  const { className, size = 'lg', isError, isReadonly, isDisabled, children, ...rest } = props;

  const yearRef = useRef<HTMLInputElement>(null);
  const monthRef = useRef<HTMLInputElement>(null);
  const dateRef = useRef<HTMLInputElement>(null);

  function handleKeyDown(event: KeyboardEvent<HTMLInputElement>) {
    if (event.key === 'ArrowRight') {
      moveRight(event);
    } else if (event.key === 'ArrowLeft') {
      moveLeft(event);
    } else if (event.key.match(/^[^0-9]$/)) {
      if (!event.ctrlKey && !event.metaKey) {
        event.preventDefault();
      }
    }
  }

  function moveRight(event: KeyboardEvent<HTMLInputElement>) {
    const input = event.target as HTMLInputElement;
    if (input.selectionStart !== input.selectionEnd) {
      return;
    }
    if (input.selectionEnd === input.value.length) {
      event.preventDefault();
      if (input === yearRef.current) {
        monthRef.current?.focus();
      } else if (input === monthRef.current) {
        dateRef.current?.focus();
      }
    }
  }

  function moveLeft(event: KeyboardEvent<HTMLInputElement>) {
    const input = event.target as HTMLInputElement;
    if (input.selectionStart !== input.selectionEnd) {
      return;
    }
    if (input.selectionStart === 0) {
      event.preventDefault();
      if (input === monthRef.current) {
        yearRef.current?.focus();
      } else if (input === dateRef.current) {
        monthRef.current?.focus();
      }
    }
  }

  return (
    // biome-ignore lint/a11y/noStaticElementInteractions: For date input navigation
    <div
      className={`inline-flex h-14 -space-x-1 rounded-8 border border-solid-gray-600 bg-[--bg] p-0.5 pe-0 text-solid-gray-900 [--bg:theme(colors.white)] focus-within:border-black hover:border-solid-gray-900 data-[size=md]:h-12 data-[size=sm]:h-10 data-[readonly]:border-dashed data-[disabled]:border-solid-gray-300 data-[error]:border-error-1 data-[disabled]:text-solid-gray-420 data-[disabled]:[--bg:theme(colors.solid-gray.50)] data-[error]:focus-within:border-red-1000 data-[error]:hover:border-red-1000 data-[error]:hover:data-[readonly]:border-error-1 hover:data-[readonly]:border-solid-gray-600 forced-colors:data-[disabled]:border-[GrayText] forced-colors:data-[disabled]:text-[GrayText] ${className ?? ''}`}
      data-size={size}
      data-error={isError || null}
      data-readonly={isReadonly || null}
      data-disabled={isDisabled || null}
      onKeyDown={handleKeyDown}
      {...rest}
    >
      {children({
        yearRef,
        monthRef,
        dateRef,
        readOnly: isReadonly,
        'aria-disabled': isDisabled,
        'aria-invalid': isError,
      })}
    </div>
  );
};
````

<!-- file: index.ts -->
````ts
export * from './DatePicker';
export * from './parts/DatePickerCalendarButton';
export * from './parts/DatePickerDate';
export * from './parts/DatePickerMonth';
export * from './parts/DatePickerYear';
````

<!-- file: parts/DatePickerCalendarButton.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';
import type { DatePickerSize } from '../DatePicker';

export type DatePickerCalendarButtonProps = ComponentProps<'button'> & {
  size?: DatePickerSize;
};

export const DatePickerCalendarButton = forwardRef<
  HTMLButtonElement,
  DatePickerCalendarButtonProps
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

<!-- file: parts/DatePickerDate.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';

export type DatePickerDateProps = Omit<ComponentProps<'input'>, 'placeholder'> & {
  placeholder?: never;
};

export const DatePickerDate = forwardRef<HTMLInputElement, DatePickerDateProps>((props, ref) => {
  const { className, 'aria-disabled': ariaDisabled, readOnly, ...rest } = props;

  return (
    <label className='relative z-0 inline-flex flex-row-reverse last:pe-4 [&:has([aria-disabled="true"])]:pointer-events-none'>
      <span className='relative z-10 self-center bg-[--bg] p-1 text-oln-16N-100'>日</span>
      <input
        className={`-me-1 w-11 rounded-8 border border-transparent bg-transparent pe-3 text-right focus:border-solid-gray-600 focus:outline focus:outline-4 focus:outline-offset-[calc(2/16*1rem)] focus:outline-black focus:ring-[calc(2/16*1rem)] focus:ring-yellow-300 aria-disabled:pointer-events-none forced-colors:border-[Canvas] forced-colors:aria-disabled:focus:border-[GrayText] ${className ?? ''}`}
        type='text'
        inputMode='numeric'
        pattern='\d+'
        readOnly={ariaDisabled === 'true' || ariaDisabled === true || readOnly}
        aria-disabled={ariaDisabled}
        ref={ref}
        {...rest}
      />
    </label>
  );
});
````

<!-- file: parts/DatePickerMonth.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';

export type DatePickerMonthProps = Omit<ComponentProps<'input'>, 'placeholder'> & {
  placeholder?: never;
};

export const DatePickerMonth = forwardRef<HTMLInputElement, DatePickerMonthProps>((props, ref) => {
  const { className, 'aria-disabled': ariaDisabled, readOnly, ...rest } = props;

  return (
    <label className='relative z-0 inline-flex flex-row-reverse last:pe-4 [&:has([aria-disabled="true"])]:pointer-events-none'>
      <span className='relative z-10 self-center bg-[--bg] p-1 text-oln-16N-100'>月</span>
      <input
        className={`-me-1 w-11 rounded-8 border border-transparent bg-transparent pe-3 text-right focus:border-solid-gray-600 focus:outline focus:outline-4 focus:outline-offset-[calc(2/16*1rem)] focus:outline-black focus:ring-[calc(2/16*1rem)] focus:ring-yellow-300 aria-disabled:pointer-events-none forced-colors:border-[Canvas] forced-colors:aria-disabled:focus:border-[GrayText] ${className ?? ''}`}
        type='text'
        inputMode='numeric'
        pattern='\d+'
        readOnly={ariaDisabled === 'true' || ariaDisabled === true || readOnly}
        aria-disabled={ariaDisabled}
        ref={ref}
        {...rest}
      />
    </label>
  );
});
````

<!-- file: parts/DatePickerYear.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';

export type DatePickerYearProps = Omit<ComponentProps<'input'>, 'placeholder'> & {
  placeholder?: never;
};

export const DatePickerYear = forwardRef<HTMLInputElement, DatePickerYearProps>((props, ref) => {
  const { className, 'aria-disabled': ariaDisabled, readOnly, ...rest } = props;

  return (
    <label className='relative z-0 inline-flex flex-row-reverse last:pe-4 [&:has([aria-disabled="true"])]:pointer-events-none'>
      <span className='relative z-10 self-center bg-[--bg] p-1 text-oln-16N-100'>年</span>
      <input
        className={`-me-1 w-16 rounded-8 border border-transparent bg-transparent pe-3 text-right focus:border-solid-gray-600 focus:outline focus:outline-4 focus:outline-offset-[calc(2/16*1rem)] focus:outline-black focus:ring-[calc(2/16*1rem)] focus:ring-yellow-300 aria-disabled:pointer-events-none forced-colors:border-[Canvas] forced-colors:aria-disabled:focus:border-[GrayText] ${className ?? ''}`}
        type='text'
        inputMode='numeric'
        pattern='\d+'
        readOnly={ariaDisabled === 'true' || ariaDisabled === true || readOnly}
        aria-disabled={ariaDisabled}
        ref={ref}
        {...rest}
      />
    </label>
  );
});
````
